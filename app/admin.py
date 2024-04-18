from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form =CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'age']

admin.site.register(CustomUser, CustomUserAdmin)

# admin.site.register(Product)
# admin.site.register(Cart)
# admin.site.register(CartItem)
# admin.site.register(Order)