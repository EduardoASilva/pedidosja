from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

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
        itens = {'nome': p.nome_cliente, 'data': p.created_at, 'produtos': {}}
        prod = Quantidade.objects.filter(id_pedido_id=p.id)
        for pr in prod:
            produto = {f"{pr.id_esfirra.nome}": f"{pr.qtd}"}
            itens['produtos'].update(produto)
        data.append(itens)

    print(data)
    # data['nome'] = pedido.nome
    # return render(request, 'comandas.html')
    return render(request, 'comandas.html', {'data': data})
