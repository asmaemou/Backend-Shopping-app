from rest_framework import serializers
from .models import cartItem

class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model= cartItem
        fields=['cartItem_ID','card_ID','quantity','quantity','subtotal']

