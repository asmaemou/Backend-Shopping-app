from django.contrib import admin
from .models import Category
from .models import Order
from .models import PaymentMethod
from .models import Product
from .models import ShippingDetail
from .models import ShoppingCart
from .models import User
from .models import WishList
from .models import NewCollection


admin.site.register(Category)
admin.site.register(Order)
admin.site.register(PaymentMethod)
admin.site.register(Product)
admin.site.register(ShippingDetail)
admin.site.register(ShoppingCart)
admin.site.register(User)
admin.site.register(WishList)
admin.site.register(NewCollection)
