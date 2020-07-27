from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class DefaultUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)


class User(models.Model):
    GENDER = {
        ('M', 'Man'),
        ('W', 'Woman'),
        ('N', 'Refusal to response'),

    }
    login = models.OneToOneField(DefaultUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=80, blank=True, null = True)
    email = models.EmailField(max_length=100)
    gender = models.CharField(choices=GENDER)

    def __str__(self):
        return str(self.login)




