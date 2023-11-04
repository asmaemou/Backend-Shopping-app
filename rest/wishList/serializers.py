from rest_framework import serializers
from .models import WishList

class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields='__all__'
