from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    model = CustomUser
    fields = UserCreationForm.Meta.fields + ("age",) #all default fields and adding custom age field

class CustomUserChangeForm(UserChangeForm):
    model = CustomUser
    fields = UserChangeForm.Meta.fields 
    #don't add custom field age, because UserCreationForm already has it (UserChangeForm add it automatically)
