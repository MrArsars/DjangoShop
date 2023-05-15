from django.urls import path

from product.views import *

urlpatterns = [
    path('product/<int:productid>/', product),
    path('product/add/', add_to_cart, name = "add"),

]
