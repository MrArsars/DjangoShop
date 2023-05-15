from django.http import HttpResponseRedirect
from django.shortcuts import render

from cart.models import CartItem
from product.models import Product


# Create your views here.
def product(request, productid):
    db_product = Product.objects.get(pk=productid)
    context = {
        'product': db_product,
    }
    return render(request, 'product/ProductPage.html', context)


def add_to_cart(request):
    if request.method == "POST" and request.user.is_authenticated:
        userId = request.user.id
        new_item = CartItem(product_id = request.POST['product_id'], user_id = userId)
        new_item.save()
    return HttpResponseRedirect(request.get_full_path())