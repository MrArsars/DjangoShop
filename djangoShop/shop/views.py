from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from shop.forms import *


# Create your views here.
#@login_required(login_url="accounts/login")
def login(request):
    return (request, 'account/login.html')