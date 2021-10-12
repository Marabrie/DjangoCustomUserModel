from django.conf import settings
from django.contrib.auth.models import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save



class CustomUser(AbstractUser):
    pass
# add additional fields here

    def __str__(self):
        return self.username


  
