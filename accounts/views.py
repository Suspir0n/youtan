from django.shortcuts import render, redirect
from accounts.forms import LoginForms, SignupForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login_view(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            name = form['name_login'].value()
            password = form['password'].value()

            username = auth.authenticate(
                request,
                username=name,
                password=password
            )

            if username is not None:
                auth.login(request, username)
                messages.success(request, f'{name} logado com sucesso!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Erro ao efetuar login')
                return redirect('login')

    return render(request, 'accounts/login.html', {'form': form})

def signup_view(request):
    form = SignupForms()

    if request.method == 'POST':
        form = SignupForms(request.POST)

        if form.is_valid():
            if form['password'].value() != form['confirm_password'].value():
                messages.error(request, 'As senhas não são iguais')
                return redirect('signup')

            name = form['name_signup'].value()
            email = form['email'].value()
            password = form['password'].value()

            if User.objects.filter(username=name).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('signup')

            usuario = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )
            usuario.save()
            messages.success(request, f'{name} cadastro com sucesso')
            return redirect('login')

    return render(request, 'accounts/signup.html', {'form': form})

def logout_view(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')
