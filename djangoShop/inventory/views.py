from django.shortcuts import render

from inventory.models import Inventory
from product.models import Product


# Create your views here.
def inventory(request):
    inventory_products = Inventory.objects.all()
    products = []
    for ip in inventory_products:
        products.append(Product.objects.get(pk=ip.product_id))

    context = {
        'products': products,
    }
    return render(request, 'inventory/InventoryPage.html', context)
