from rest_framework import serializers
from .models import ShoppingCart

class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model= ShoppingCart
        fields='__all__'