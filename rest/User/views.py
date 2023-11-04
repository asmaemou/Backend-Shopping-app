from rest_framework.viewsets import ModelViewSet
from .serializers import RestSerializer
from .models import User

class ShoppingCartView(ModelViewSet):
    serializer_class = RestSerializer
    def get_queryset(self):
        return User.objects.all()