from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User


class UserRegistration(UserCreationForm):

    class Meta:
        model = User
        fields = ['login', 'name']