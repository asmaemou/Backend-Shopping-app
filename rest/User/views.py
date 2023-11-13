from rest_framework.viewsets import ModelViewSet
from .serializers import RestSerializer
from .models import User

class UserView(ModelViewSet):
    serializer_class = RestSerializer
    queryset=User.objects.all()