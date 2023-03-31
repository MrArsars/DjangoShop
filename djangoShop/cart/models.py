from django.db import models
from product.models import Product
from shop.models import CustomUser


# Create your models here.
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
