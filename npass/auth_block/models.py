# models.py (в вашем приложении, например, 'users' или 'auth_block')
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email обязателен')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    """
    Кастомная модель пользователя с дополнительными полями
    """
    # Дополнительные поля
    username = models.CharField(max_length=150, unique=False, blank=True, null=True)

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
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'custom_users'  # Явно указываем имя таблицы
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
