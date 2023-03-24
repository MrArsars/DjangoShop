from django.db import models

from product.models import Product


# Create your models here.
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
