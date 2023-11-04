from django.db import models
from ..ShoppingCart.models import ShoppingCart
from ..Product.models import Product

class CartItem(models.Model):
    
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product + ' ' + self.quantity