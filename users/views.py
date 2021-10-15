from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from blog.settings import LOGOUT_REDIRECT_URL


def logout_view():
    return LOGOUT_REDIRECT_URL


def register(request):
    """Faz o cadastro de um novo usuário."""
    if request.method != 'POST':
        # Exibe o formulário de cadastro em branco
        form = UserCreationForm()
    else:
        # Processa o formulário preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Faz login do usuário e o redireciona para a página inicial
            authenticated_user = authenticate(
                username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return redirect('index')

    context = {'form': form, 'page_name': 'create account'}
    return render(request, 'registration/register.html', context)
