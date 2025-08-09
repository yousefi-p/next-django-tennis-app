from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
from datetime import timedelta
import random

class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('شماره تماس الزامی است.')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='شماره تماس')
    fullname = models.CharField(max_length=30, verbose_name='نام')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_player = models.BooleanField(default=True, verbose_name='بازیکن')
    is_staff = models.BooleanField(default=False, verbose_name='مربی')
    is_manager = models.BooleanField(default=False, verbose_name='مدیر')
    is_superuser = models.BooleanField(default=False, verbose_name='ادمین')

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number
    

class SMSCode(models.Model):
    phone_number = models.CharField(max_length=11, verbose_name='شماره تماس')
    code = models.CharField(max_length=6, verbose_name='کد تایید')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=5)

    @staticmethod
    def generate_code():
        return str(random.randint(100000, 999999))
