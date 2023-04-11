from django.shortcuts import render

from cart.models import CartItem
from product.models import Product


# Create your views here.
def shopping_cart(request):
    userId = None
    db_product = []
    if request.user.is_authenticated:
        userId = request.user.id
        cartItems = CartItem.objects.filter(user_id=userId)
        for item in cartItems:
            db_product.append(Product.objects.get(pk=item.product_id))
    context = {
        'cartItems': db_product
    }
    return render(request, 'cart/Cart.html', context)
