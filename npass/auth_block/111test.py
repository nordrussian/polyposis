# auth_block/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from .models import CustomUser


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = CustomUser  # 👈 ГЛАВНОЕ: указываем CustomUser
        fields = ("username", "email")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['email'].required = True
        
        for name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"