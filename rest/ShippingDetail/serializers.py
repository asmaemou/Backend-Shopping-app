from rest_framework import serializers
from .models import ShippingDetail

class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingDetail
        fields='__all__'
