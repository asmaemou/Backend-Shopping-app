from rest_framework import serializers
from .models import cartItem

class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model= cartItem
        fields='__all__'

