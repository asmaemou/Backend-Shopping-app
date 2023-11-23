from rest_framework.viewsets import ModelViewSet
from .serializers import RestSerializer
from .models import User

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RestSerializer
