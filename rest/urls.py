from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .Product.views import ProductView  
from .CartItem.views import CartItemView  
from .Category.views import CategoryView  
from .Order.views import OrderView  
from .PaymentMethod.views import PaymentMethodView 
from .ShippingDetail.views import ShippingDetailView 
from .ShoppingCart.views import ShoppingCartView 


router = routers.DefaultRouter()
router.register(r'products', ProductView,basename='products')
router.register(r'cartitems', CartItemView, basename='cartitems')
router.register(r'categories', CategoryView, basename='categories')
router.register(r'orders', OrderView, basename='orders')
router.register(r'paymentsmethod', PaymentMethodView, basename='paymentsmethod')
router.register(r'shippingdetails', ShippingDetailView, basename='shippingdetails')
router.register(r'shoppingcarts', ShoppingCartView, basename='shoppingcarts')

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += router.urls
