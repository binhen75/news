from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm #creation
    form = CustomUserChangeForm #editing
    model = CustomUser
    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields" : ("age",)}),) #editing
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),) #creation

admin.site.register(CustomUser, CustomUserAdmin)