from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=255, null=False, blank=False)
    is_owner = models.BooleanField(default=True)