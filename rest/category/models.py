from django.db import models

class Category(models.Models):
    category_ID=models.CharField(max_length=20, primary_key=True)
    category_Name = models.CharField(max_length=50)
    category_Description=models.CharField(max_length=40)

    def __str__(self):
        return self.category_ID