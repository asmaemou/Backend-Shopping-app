from django.db import models
from ..Users.models import User

class shoppingCarts(models.Model):

    cart = models.CharField(max_length=20, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    total_price = models.CharField(max_length=20)
    date_added = models.CharField(max_length=20)

    def __str__(self):
        return self.cart + self.total_price
