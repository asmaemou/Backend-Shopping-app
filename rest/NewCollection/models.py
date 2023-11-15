from django.db import models

class NewCollection(models.Model):
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    amount = models.DecimalField(max_digits=19, decimal_places=10,default=0.00)


