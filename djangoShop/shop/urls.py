from django.urls import path
from allauth.account.views import LoginView

from shop.views import *

urlpatterns = [
    path('home', home),
    path('', LoginView.as_view()),
]
