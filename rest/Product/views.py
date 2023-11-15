from rest_framework.viewsets import ModelViewSet
from .serializers import RestSerializer
from .models import Product

class ProductView(ModelViewSet):
    serializer_class = RestSerializer
    queryset = Product.objects.all()
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
