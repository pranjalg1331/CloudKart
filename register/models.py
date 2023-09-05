from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import ProfileManager
# Create your models here.
class Profile(AbstractUser):
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=100,unique=True)
    is_authenticated=models.BooleanField(default=False)
    token=models.CharField(max_length=200,null=True)
    
    REQUIRED_FIELDS=['username','phone']
    USERNAME_FIELD="email"
    
    objects= ProfileManager()
