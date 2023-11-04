from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .Product.views import ProductView  # Assuming it's a ViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductView,basename='products')

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns +=router.urls
