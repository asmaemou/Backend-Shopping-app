from rest_framework import serializers
from .models import Order

class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['order_ID','card_ID','user_ID','order_status','order_date','shipping_address','billing_address','tracking_number']
