from rest_framework.viewsets import ModelViewSet
from .serializers import RestSerializer
from .models import ShippingDetails

class ShippingDetailsView(ModelViewSet):
    serializer_class = RestSerializer
    def get_queryset(self):
        return ShippingDetails.objects.all()