from django.urls import path
from allauth.account.views import LoginView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from shop.views import *

urlpatterns = [
    path('home', home),
    path('', LoginView.as_view()),
]
urlpatterns += staticfiles_urlpatterns()
