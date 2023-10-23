from rest_framework import serializers
from .models import Category

class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['category_ID','category_Name','category_Description']
