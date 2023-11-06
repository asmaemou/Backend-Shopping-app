from django.db import models
from ..Category.models import Category  
from pictures.models import PictureField


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    product_Description = models.CharField(max_length=20)
    product_Stock = models.CharField(max_length=20)
    product_Rating = models.CharField(max_length=20)
    # product_picture = models.CharField(max_length=20)
    product_name = models.CharField(max_length=20)
    product_price = models.CharField(max_length=20)
    product_status = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=20)
    picture = PictureField(upload_to="rest/avatars",null=True,blank=True)
    picture_width = models.PositiveIntegerField(default=0)
    picture_height = models.PositiveIntegerField(default=0)  

    def __str__(self) :
        return self.product_Description
