from rest_framework.viewsets import ModelViewSet
from .serializers import RestSerializer
from .models import Category

class CategoryView(ModelViewSet):
    serializer_class = RestSerializer
    def get_queryset(self):
        return Category.objects.all()