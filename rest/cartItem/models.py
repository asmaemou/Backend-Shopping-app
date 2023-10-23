from django.db import models
from django.contrib.auth.models import shoppingCart,product

class CartItem(models.Model):
    cartItem_ID=models.CharField(max_length=20, primary_key=True)
    card_ID=models.ForeignKey(shoppingCart,on_delete=models.CASCADE)
    quantity=models.charField(max_length=20)
    procuct_ID=models.ForeignKey(product,on_delete=models.CASCADE)
    subtotal=models.CharField(max_length=20)

    def __str(self):
        return self.cartItem_ID