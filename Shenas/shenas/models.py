from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    CLIENT = 'client', 'Client'


class User(AbstractUser):
    phone = models.CharField(max_length=12)
    role = models.CharField(max_length=6, choices=UserRole.choices, default=UserRole.CLIENT)
