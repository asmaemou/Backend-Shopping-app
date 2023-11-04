from rest_framework.viewsets import ModelViewSet
from .serializers import RestSerializer
from .models import WishList

class WishListView(ModelViewSet):
    serializer_class = RestSerializer
    def get_queryset(self):
        return WishList.objects.all()