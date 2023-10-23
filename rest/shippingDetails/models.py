from django.db import models
from ..order.models import Order

class ShippingDetails(models.Model):
    shipping_ID=models.CharField(max_length=20, primary_key=True)
    order_ID=models.ForeignKey(Order,on_delete=models.CASCADE)
    shipping_method=models.CharField(max_length=20)
    shipping_cost=models.CharField(max_length=20)
    estimated_delivery=models.CharField(max_length=20)

    def __str__(self):
        self.shipping_ID