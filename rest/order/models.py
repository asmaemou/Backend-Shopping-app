from django.db import models
from ..shoppingCarts.models import shoppingCarts 
from ..users.models import users


class Order(models.Model):
    order_ID=models.charField(max_length=20)
    card_ID=models.ForeignKey(shoppingCarts,on_delete=models.CASCADE)
    user_ID=models.ForeignKey(users,on_delete=models.CASCADE)
    order_status=models.charField(max_length=20)
    order_date=models.charField(max_length=20)
    shipping_address=models.charField(max_length=20)
    billing_address=models.charField(max_length=20)
    tracking_number=models.charField(max_length=20)

    def __str__(self):
        return self.order_ID
    
