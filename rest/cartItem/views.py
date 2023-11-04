from rest_framework.viewsets import ModelViewSet
from .serializers import RestSerializer
from .models import CartItem

class CartItemView(ModelViewSet):
    serializer_class = RestSerializer
    def get_queryset(self):
        return CartItem.objects.all()