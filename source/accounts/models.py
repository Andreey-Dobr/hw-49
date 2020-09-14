from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

class Profile(models.Model):
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    profile = models.EmailField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.user.get_full_name() + "'s Profile"
