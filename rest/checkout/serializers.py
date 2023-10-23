from rest_framework import serializers
from .models import checkout

class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model= checkout
        fields=['cardID','paymentID']