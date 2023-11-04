from django.db import models
from ..shoppingCart.models import ShoppingCart
from ..product.models import Product

class CartItem(models.Model):
    
    cart=models.ForeignKey(ShoppingCart,on_delete=models.CASCADE)
    quantity=models.charField(max_length=20)
    procuct=models.ForeignKey(Product,on_delete=models.CASCADE)
    subtotal=models.CharField(max_length=20)

    def __str(self):
        return self.product + self.quantity