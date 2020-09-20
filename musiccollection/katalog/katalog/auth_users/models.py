from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    GENDER = {
        ('M', 'Man'),
        ('W', 'Woman'),
        ('N', 'Refusal to response'),

    }

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null = True,  help_text='Optional.')
    last_name = models.CharField(max_length=30, blank=True, null = True, help_text='Optional.')
    email = models.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    gender = models.CharField(choices=GENDER, max_length=10)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()




