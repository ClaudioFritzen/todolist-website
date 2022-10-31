from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import todo


# Create your views here.
def home(request):
    if request.method == "POST":
        task = request.POST.get('task')
        new_todo = todo(user=request.user, todo_name=task )
        new_todo.save()
    return render(request, 'todoapp/todo.html', {})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        #validação da senha
        if len(password) < 7:
            messages.error(request, 'Senha deve conter 7 ou mais caracteres!!')
            return redirect('register')

        #fazendo um filtro no db e vendo se existe esse usuario
        get_all_user_username = User.objects.filter(username=username)
        if get_all_user_username:
            messages.error(request, 'Erro ao criar usuario, usuario já existe!!')
            return redirect('register')

        # se as validações estiverem ok, save no db.
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        
        # mostrar mms de usuario criado.
        messages.success(request, 'Usuario criado com sucesso, faça login')
        # apos salvar no db vamos para a pag de login
        return redirect('login')

        #print(username, email, password)
    return render(request, 'todoapp/register.html', {})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        # fazendo a validacao de autenticcao no db
        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home-page')

        else:
            messages.error(request, 'Usuario ou senha estão errado!')
            return redirect('login')

    return render(request, 'todoapp/login.html', {})