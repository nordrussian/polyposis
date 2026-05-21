
from django.urls import path, include
from django.views.generic import TemplateView

from .views import (
    RegisterView,
)

app_name = "auth_block"

urlpatterns = [
        path("register/", RegisterView.as_view(), name="register"),
        path('202/', TemplateView.as_view(template_name='auth_block/202.html'), name='registration_success'),
]

