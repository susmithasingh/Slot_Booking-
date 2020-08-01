from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser, models.Model):
   role = models.BooleanField(default=False)