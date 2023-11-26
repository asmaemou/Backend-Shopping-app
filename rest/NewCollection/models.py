from django.db import models

class NewCollection(models.Model):

    # picture = models.ImageField(upload_to='images/', null=True, blank=True)
    # amount = models.DecimalField(max_digits=19, decimal_places=2,default=0.00)
    # name = models.CharField(max_length=20)


    description = models.CharField(max_length=20,default="no description")
    stock = models.IntegerField(default=1)
    rating = models.IntegerField(default=1)
    name = models.CharField(max_length=20,default="no name")
    amount = models.DecimalField(max_digits=19, decimal_places=2,default=0.00)
    status = models.CharField(max_length=20,default="no satus")
    manufacturer = models.CharField(max_length=20,default="no manufacturer")
    quantity = models.IntegerField(default=1)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
      

    def __str__(self) :
        return self.description

