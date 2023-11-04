from django.db import models
from ..ShoppingCarts.models import ShoppingCarts 
from ..Users.models import Users


class Order(models.Model):

    cart = models.ForeignKey(ShoppingCarts,on_delete=models.CASCADE)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    order_status = models.charField(max_length=20)
    order_date = models.charField(max_length=20)
    shipping_address = models.charField(max_length=20)
    billing_address = models.charField(max_length=20)
    tracking_number = models.charField(max_length=20)

    def __str__(self):
        return self.cart + self.tracking_number
    
