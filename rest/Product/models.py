from django.db import models
from ..Category.models import Category  


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    description = models.CharField(max_length=20)
    stock = models.CharField(max_length=20)
    rating = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=19, decimal_places=2,default=0.00)
    status = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
      

    def __str__(self) :
        return self.description
