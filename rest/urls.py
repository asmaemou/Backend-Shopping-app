from django.contrib import admin
from django.urls import path, include
from pictures.conf import get_settings
from rest_framework import routers
from .Product.views import ProductView  
from .CartItem.views import CartItemView  
from .Category.views import CategoryView  
from .Order.views import OrderView  
from .PaymentMethod.views import PaymentMethodView 
from .ShippingDetail.views import ShippingDetailView 
from .ShoppingCart.views import ShoppingCartView
from .WishList.views import WishListView


router = routers.DefaultRouter()
router.register(r'products', ProductView,basename='products')
router.register(r'cartitems', CartItemView, basename='cartitems')
router.register(r'categories', CategoryView, basename='categories')
router.register(r'orders', OrderView, basename='orders')
router.register(r'paymentsmethod', PaymentMethodView, basename='paymentsmethod')
router.register(r'shippingdetails', ShippingDetailView, basename='shippingdetails')
router.register(r'shoppingcarts', ShoppingCartView, basename='shoppingcarts')
router.register(r'wishlists', WishListView, basename='wishlists')


urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += router.urls

if get_settings().USE_PLACEHOLDERS:
    urlpatterns += [
        path("_pictures/", include("pictures.urls")),
    ]