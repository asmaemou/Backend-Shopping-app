from rest_framework import serializers
from .models import NewCollection

class RestSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewCollection
        fields = '__all__'