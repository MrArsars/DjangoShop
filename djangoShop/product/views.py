from django.shortcuts import render

from product.models import Product


# Create your views here.
def product(request, productid):
    db_product = Product.objects.get(pk=productid)
    context = {
        'product': db_product,
    }
    return render(request, 'product/ProductPage.html', context)
