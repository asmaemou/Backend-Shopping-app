from rest_framework import serializers
from .models import users

class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model= users
        fields=['id','name','description']