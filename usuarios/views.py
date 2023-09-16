from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render

from usuarios.forms import LoginForms

from django.contrib import auth


# Create your views here.

def login(request):

    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)
        
       

        if form.is_valid():
            print("Formulário válido")
            nome = form['nome_login'].value()
            senha = form['senha'].value()
            print(nome)
            print(senha)
        else:
            print("Formulário inválido")
            print(form.errors)
            return render(request, 'usuarios/login.html', {"form" : form})
                
           

        usuario = auth.authenticate(
            request, 
            username=nome, 
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            print("Usuário autenticado")
            return redirect('admin:index')
                  
        else:
            return redirect('login')


                

    return render(request, 'usuarios/login.html', {"form" : form})

