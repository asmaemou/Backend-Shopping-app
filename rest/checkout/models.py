from django.db import models

class checkout(models.Model):
    cardID=models.CharField(max_length=20)
    paymentID=models.CharField(max_length=20)
    


    def __str__(self) :
        return self.cardID
        return self.paymentID
