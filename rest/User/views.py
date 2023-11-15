from rest_framework.viewsets import ModelViewSet
from .serializers import RestSerializer
from .models import User

class UserView(ModelViewSet):
    serializer_class = RestSerializer
    def get_queryset(self):
        return super().get_queryset()