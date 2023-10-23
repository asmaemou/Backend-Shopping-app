from django.db import models
from ..User.models import User
from ..Product.models import Product


class WishList(models.Model):
    WishList_ID=models.CharField(max_length=20,primary_key= True)
    user_ID=models.ForeignKey(User,on_delete=models.CASCADE)
    product_ID=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.WishList_ID
