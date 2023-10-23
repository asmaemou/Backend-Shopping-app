from django.db import models

class paymentMethod(models.Model):
    paymentID=models.CharField(max_length=20)
    cvv=models.CharField(max_length=20)
    expiringDate=models.CharField(max_length=20)
    cardNumber=models.CharField(max_length=20)


    def __str__(self) :
        return self.paymentID
