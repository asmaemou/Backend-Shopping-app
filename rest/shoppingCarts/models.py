from django.db import models
from ..users.models import User  # Import the User model from Django's built-in auth system

class shoppingCarts(models.Model):
    cartID = models.CharField(max_length=20, primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)  # Use ForeignKey to establish the relationship
    total_price = models.CharField(max_length=20)
    date_added = models.CharField(max_length=20)

    def __str__(self):
        return self.cartID
