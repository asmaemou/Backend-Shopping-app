from django.db import models
from ..Order.models import Order

class ShippingDetail(models.Model):

    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    shipping_method = models.CharField(max_length=20)
    shipping_cost = models.CharField(max_length=20)
    estimated_delivery = models.CharField(max_length=20)

    def __str__(self):
        return self.shipping_method + ' '+ self.order