from django.db import models
from django.contrib.auth.models import AbstractUser

from .utilities import get_timestamp_path

class AdvUser(AbstractUser):
    about = models.TextField(default='', blank=True, verbose_name='О себе')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Аватар')
    class Meta(AbstractUser.Meta):
        pass