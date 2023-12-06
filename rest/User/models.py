from django.db import models
from django.forms import JSONField

class User(models.Model):

    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)



    def __str__(self) :
        return self.fname + ' '+ self.lname
