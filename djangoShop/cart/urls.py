from django.urls import path
from cart.views import *

urlpatterns = [
    path('cart/', shopping_cart),
]