from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .Product.views import ProductView
from .PaymentMethod.views import PaymentMethodView

router = routers.DefaultRouter()
router.register("/Product", ProductView, basename="Product")
router.register("/PaymentMethod", PaymentMethodView, basename="PaymentMethod")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include the URLs generated by the router under the 'api/' path.
]
urlpatterns = router.urls
