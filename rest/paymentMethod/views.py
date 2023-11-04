from rest_framework.viewsets import ModelViewSet
from .serializers import RestSerializer
from .models import PaymentMethod

class PaymentMethodView(ModelViewSet):
    serializer_class = RestSerializer
    # list the product of a specific user
    def get_queryset(self):
        return PaymentMethod.objects.all()