from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.utils import timezone

# cutom manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email=self.normalize_email(email)
        user=self.model(email=email, **extra_fields)
        user.set_password(password) #hash password
        user.save(using=self._db)
        return user
    
    # def create_superuser(self, email, password, **extra_fields):
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    #     return self.create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self.create_user(email, password, **extra_fields)


# cutom user model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    date_joined=models.DateTimeField(default=timezone.now)


    objects= CustomUserManager() #user our customer manager

    USERNAME_FIELD='email' # use email instead of username
    REQUIRED_FIELDS= ['first_name', 'last_name']

    def __str__(self):
        return self.email