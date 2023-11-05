from django.db import models
from ..ShoppingCart.models import ShoppingCart
from ..User.models import User


class Order(models.Model):

    cart = models.ForeignKey(ShoppingCart,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order_status = models.CharField(max_length=20)
    order_date = models.DateField()
    shipping_address = models.CharField(max_length=20)
    billing_address = models.CharField(max_length=20)
    tracking_number = models.CharField(max_length=20)

    def __str__(self):
        return self.tracking_number

