from rest_framework.viewsets import ModelViewSet
from .serializers import RestSerializer
from .models import ShippingDetail

class ShippingDetailView(ModelViewSet):
    serializer_class = RestSerializer
    queryset = ShippingDetail.objects.all()