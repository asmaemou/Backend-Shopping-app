from rest_framework.viewsets import ModelViewSet
from .serializers import RestSerializer
from .models import CartItem

class CartItemView(ModelViewSet):
    serializer_class = RestSerializer
    queryset = CartItem.objects.all()