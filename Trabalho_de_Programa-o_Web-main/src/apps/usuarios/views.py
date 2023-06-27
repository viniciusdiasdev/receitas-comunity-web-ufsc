from email import message
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request, 'o campo nome não pode ficar em branco')
            return redirect('cadastro')

        if campo_vazio(email):
            messages.error(request, 'o campo email não pode ficar em branco')
            return redirect('cadastro')

        if senhas_nao_iguais(senha, senha2):
            messages.error(request, 'As Senhas não são iguais, ou nulas')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-Mail já cadastrado')
            return redirect('cadastro')

        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuario já cadastrado')
            return redirect('cadastro')

        user = User.objects.create_user(
            username=nome, email=email, password=senha)

        user.save()
        messages.success(request, 'Conta criada com sucesso')

        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Campos vazios')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(
                email=email).values_list('username', flat=True).get()


            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('login realizado com sucesso')
                return redirect('dashboard')

    return render(request, 'usuarios/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by(
            '-date_categoria').filter(pessoa=id)
        dados = {
            'receitas': receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def atualiza_cadastro(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            nome = request.POST['nome']
            senha = request.POST['password']
            senha2 = request.POST['password2']

            if senhas_nao_iguais(senha, senha2):
                messages.error(request, 'As Senhas não são iguais, ou nulas')
                return redirect('atualiza_cadastro')

            id = request.user.id
            usuario = get_object_or_404(User, id=id)

            usuario.username = nome
            usuario.set_password(senha)
            usuario.save()
            messages.success(request, 'Conta alterada com sucesso')

            return redirect('login')
        
    elif request.user.is_authenticated:
        id = request.user.id
        usuario = get_object_or_404(User, id=id)
        print(usuario.username)
        print(usuario.email)
        dados = {
            'usuario':usuario
        }

        return render(request, 'usuarios/atualizacao.html', dados)
    
    else:
        return redirect('index')
        

def campo_vazio(campo):
    return not campo.strip()


def senhas_nao_iguais(senha1, senha2):
    return senha1 != senha2

