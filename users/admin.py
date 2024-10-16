from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fields = ['first_name', 'last_name', 'password', 'email']
    list_display = ['first_name', 'last_name', 'email']
    list_display_links = ['first_name', 'email'] 
