from django.db import models
from ..category.models import Category  


class Product(models.Model):
    product_ID=models.CharField(max_length=20, primary_key=True)
    product_Category_ID=models.ForeignKey(Category, on_delete=models.CASCADE)  
    product_Description=models.CharField(max_length=20)
    product_Stock=models.CharField(max_length=20)
    product_Rating=models.CharField(max_length=20)
    product_picture=models.CharField(max_length=20)
    product_name=models.CharField(max_length=20)
    product_price=models.CharField(max_length=20)
    product_status=models.CharField(max_length=20)
    manufacturer=models.CharField(max_length=20)
  

    def __str__(self) :
        return self.product_ID
