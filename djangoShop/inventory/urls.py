from django.urls import path
from allauth.account.views import LoginView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from inventory.views import *

urlpatterns = [
    path('inventory', inventory),
]
urlpatterns += staticfiles_urlpatterns()
