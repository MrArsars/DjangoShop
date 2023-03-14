from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import make_password
from django.shortcuts import render

from shop.forms import *


# Create your views here.
def home(request):
    return render(request, 'Home.html')


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()

    return render(request, 'Auth.html', {'form': form, 'title': 'Register', 'user': '', 'error': ''})


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(username=username)
        except:
            return render(request, 'Auth.html', {'form': form, 'title': 'Login',
                                                 'error': f'No user ',
                                                 'user': ''})

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return render(request, 'Auth.html', {'form': form, 'title': 'Login', 'user': f'{username}', 'error': ''})
        else:
            return render(request, 'Auth.html', {'form': form, 'title': 'Login',
                                                 'error': f'Wrong credentials ',
                                                 'user': ''})



    else:
        return render(request, 'Auth.html', {'form': form, 'title': 'Login', 'error': '', 'user': ''})
