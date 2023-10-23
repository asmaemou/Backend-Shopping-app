from rest_framework import serializers
from .models import Product

class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields=['productID','product_Category_ID','product_Description','product_Stock','product_Rating','product_picture','product_name','product_price','product_status','manufacturer']
