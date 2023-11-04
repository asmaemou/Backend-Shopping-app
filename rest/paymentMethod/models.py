from django.db import models

class PaymentMethod(models.Model):

    cvv = models.CharField(max_length=20)
    expiringDate = models.CharField(max_length=20)
    cardNumber = models.CharField(max_length=20)

    def __str__(self) :
        return self.cardNumber + ' '+ self.cvv
