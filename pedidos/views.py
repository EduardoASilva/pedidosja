from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse


@login_required(login_url='login')
def index(request):
    return render(request, 'admpage.html')


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
