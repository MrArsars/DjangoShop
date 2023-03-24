from django.urls import path, include
from allauth.account.views import LoginView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from shop.views import *

urlpatterns = [
    #path('', LoginView.as_view()),
    path("", include("allauth.account.urls"))
]
urlpatterns += staticfiles_urlpatterns()
