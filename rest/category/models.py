from django.db import models

class Category(models.Model):
    
    category_Name = models.CharField(max_length=50)
    category_Description=models.CharField(max_length=40)

    def __str__(self):
        return self.category_Name