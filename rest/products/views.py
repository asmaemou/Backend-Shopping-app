from rest_framework.viewsets import ModelViewSet
from .serializers import RestSerializer
from .models import Product

class ProductView(ModelViewSet):
    serializer_class = RestSerializer
    # list the product of a specific user
    def get_queryset(self):
        return Product.objects.all()