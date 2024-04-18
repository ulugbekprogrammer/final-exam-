from django.urls import path
from .views import *

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    path('home/', Home.as_view(), name='home'),
    path('shop/', shop, name='shop'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/', cart, name='cart'),
    path('cart/delete/<int:cart_item_id>/', delete_cart_item, name='delete_cart_item'),
    path('checkout/', checkout, name='checkout'),
    path('order/success/', order_success, name='order_success'),
    path('details/', detail, name='details'),
    path('compare/', compare, name='compare'),
    path('accounts/', accounts, name='accounts'),
]