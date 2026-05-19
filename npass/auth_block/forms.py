from django.contrib.auth.forms import (
    AuthenticationForm as AuthenticationFormGeneric,
    UserCreationForm as UserCreationFormGeneric, UserChangeForm
)
from django import forms
from .models import CustomUser


class AuthenticationForm(AuthenticationFormGeneric):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field: forms.Field
            widget: forms.Widget = field.widget
            widget.attrs["class"] = "form-control"


class UserCreationForm(UserCreationFormGeneric):
    class Meta:
        model = CustomUser
        fields = "username", "email"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].required = True

        for name, field in self.fields.items():
            field: forms.Field
            widget: forms.Widget = field.widget
            widget.attrs["class"] = "form-control"

class UserCreationForm(UserCreationFormGeneric):
    class Meta:
        model = CustomUser  # 👈 ПОЛНОСТЬЮ ПЕРЕОПРЕДЕЛЯЕМ, а не наследуем
        fields = ("username", "email")
        # Можно добавить другие настройки Meta по необходимости
        # help_texts = {...}
        # error_messages = {...}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['email'].required = True
        
        for name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

class UserCreationForm(UserCreationFormGeneric):

    class Meta:
        model = CustomUser
        fields = ("username")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username")