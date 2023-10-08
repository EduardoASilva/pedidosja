from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from pedidos.models import Pedidos, Esfirras, Quantidade


@login_required(login_url='login')
def index(request):
    esfirras = Esfirras.objects.filter(ativo=True)
    return render(request, 'admpage.html', {'esfirras': esfirras})


# Create your views here.
def login(request):
    return render(request, 'login.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()

        if not email or not password:
            messages.error(request, 'Campos vazios!')
            return redirect('login')

        user = User.objects.filter(email__iexact=email).last()
        if user:
            if user.check_password(password):
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, f'Bem Vindo {user.username}')
                    return redirect('index')
                else:
                    messages.warning(request, 'Usuário inativo.')
                    return redirect('login')
            else:
                messages.warning(request, 'Email ou Senha incorreto.')
                return redirect('login')
        else:
            messages.warning(request, 'Email ou Senha incorreto.')
            return redirect('login')
    else:
        return redirect('login')


def logout(request):
    auth.logout(request)
    return redirect('login')


def enviar_pedido(request):
    if request.method == 'POST':
        if request.POST.get('id_pedido'):
            pedido = Pedidos.objects.filter(pk=request.POST.get('id_pedido')).last()
            qtd = Quantidade.objects.filter(id_pedido_id=pedido.id)
            for key, value in request.POST.items():
                if key != 'csrfmiddlewaretoken' and key != 'nome' and key != 'id_pedido':
                    # id_esfirra = Esfirras.objects.filter(nome__contains=key.lower()).last().id
                    for q in qtd:
                        if q.id_esfirra.nome == key:
                            q.qtd = int(value)
                            q.save()
            return redirect('comandas')
        else:
            try:
                pedido = Pedidos.objects.create(
                    nome_cliente=request.POST.get('nome'),
                    id_user_id=request.user.id
                )
            except Exception as e:
                messages.error(request, f'Erro: {e.args}')
                return render(request, 'admpage.html')

            data = {}
            for key, value in request.POST.items():
                if key != 'csrfmiddlewaretoken' and key != 'nome':
                    id_esfirra = Esfirras.objects.filter(nome__contains=key.lower()).last().id
                    data['id_pedido_id'] = pedido.id
                    data['id_esfirra_id'] = id_esfirra
                    data['qtd'] = value

                    Quantidade.objects.create(**data)

            messages.success(request, 'Pedido criado com sucesso!')
            esfirras = Esfirras.objects.filter(ativo=True)
            return redirect('index')


def comandas(request):
    pedidos = Pedidos.objects.filter(finalizado=False)
    data = []
    for p in pedidos:
        itens = {'id': p.id, 'nome': p.nome_cliente, 'data': p.created_at, 'produtos': {}}
        prod = Quantidade.objects.filter(id_pedido_id=p.id)
        for pr in prod:
            produto = {f"{pr.id_esfirra.nome}": f"{pr.qtd}"}
            itens['produtos'].update(produto)
        data.append(itens)

    return render(request, 'comandas.html', {'data': data})


def finalizar_pedido(request, id_pedido):
    if request.method == 'GET':
        try:
            pedido = Pedidos.objects.filter(pk=id_pedido).get()
            pedido.finalizado = True
            pedido.save()
            data = {
                'success': True,
                'nome': pedido.nome_cliente
            }
            return JsonResponse(data)
        except Exception as e:
            data = {
                'success': False,
                'msg': f'Erro ao finalizar pedido "{e.args}"!'
            }
            return JsonResponse(data)


def relatorio(request):
    pedido = Pedidos.objects.filter(finalizado=True)

    carne = 0
    queijo = 0
    morango = 0

    for p in pedido:
        itens = Quantidade.objects.filter(id_pedido_id=p.id)
        for i in itens:
            if i.id_esfirra.nome == 'Carne':
                carne += i.qtd
            elif i.id_esfirra.nome == 'Queijo':
                queijo += i.qtd
            elif i.id_esfirra.nome == 'Morango':
                morango += i.qtd

    valor_total = carne + queijo + morango * 5
    valor_total = f'R${valor_total:_.2f}'
    valor_total = valor_total.replace('.', ',').replace('_', '.')
    print(f'O lucro foi de {valor_total}')

    context = {
        'carne': carne,
        'queijo': queijo,
        'morango': morango,
        'pedidos': pedido.count(),
        'valor_total': valor_total
    }

    return render(request, 'relatorio.html', context)
