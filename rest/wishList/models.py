from django.db import models
from ..User.models import User
from ..Product.models import Product


class WishList(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.user + ' '+ self.product
