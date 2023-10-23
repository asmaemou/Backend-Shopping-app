from rest_framework import serializers
from .models import paymentMethod

class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model= paymentMethod
        fields=['paymentID','cvv','expiringDate','cardNumber']