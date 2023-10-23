from rest_framework import serializers
from .models import shoppingCarts

class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model= shoppingCarts
        fields=['cartID','paymentMethod','cartNumber']