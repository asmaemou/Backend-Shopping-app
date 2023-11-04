from rest_framework.viewsets import ModelViewSet
from .serializers import RestSerializer
from .models import ShoppingCart

class ShoppingCartView(ModelViewSet):
    serializer_class = RestSerializer
    queryset=ShoppingCart.objects.all()