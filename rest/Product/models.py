from django.db import models
from ..Category.models import Category  


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    description = models.CharField(max_length=20)
    stock = models.CharField(max_length=20)
    rating = models.CharField(max_length=20)
    # product_picture = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=20)
    # picture = models.ProductField(upload_to="images/", null=True, blank=True)
      

    def __str__(self) :
        return self.description
