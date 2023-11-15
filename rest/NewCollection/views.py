from rest_framework.viewsets import ModelViewSet
from .serializers import RestSerializer
from .models import NewCollection

class NewCollectionView(ModelViewSet):
    serializer_class = RestSerializer
    queryset = NewCollection.objects.all()
    
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)
