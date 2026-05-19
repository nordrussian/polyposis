# models.py (в вашем приложении, например, 'users' или 'auth_block')
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Кастомная модель пользователя с дополнительными полями
    """
    # Дополнительные поля
    
    phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    expierence = models.TextField(max_length=500, blank=True) #опыт
    #diploma = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    # Вы можете переопределить обязательные поля
    email = models.EmailField(unique=True)  # Email должен быть уникальным
    
    # Статусы (например, для верификации)
    is_verified = models.BooleanField(default=False)
    
    # Дата создания (автоматически)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'custom_users'  # Явно указываем имя таблицы
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

# Create your models here.
