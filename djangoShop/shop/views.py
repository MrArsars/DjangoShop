from django.http import HttpResponse
from django.shortcuts import render

from shop.forms import RegisterForm


# Create your views here.
def home(request):
    return render(request, 'Home.html')


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'Register.html', {'form': form})
