from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model=Profile
        fields = ['username','phone', 'email', 'password1', 'password2']
        

