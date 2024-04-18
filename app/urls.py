from django.urls import path
from .views import *

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    path('home/', Home.as_view(), name='home'),
    path('shop/', shop, name='shop'),
    path('details/', detail, name='detail'),
    path('compare/', compare, name='compare'),
    path('accounts/', accounts, name='accounts'),
]