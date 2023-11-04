from rest_framework.viewsets import ModelViewSet
from .serializers import RestSerializer
from .models import Order

class OrderView(ModelViewSet):
    serializer_class = RestSerializer
    def get_queryset(self):
        return Order.objects.all()