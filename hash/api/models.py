from django.db import models
from . manager import UserManager
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(verbose_name="First Name",  max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Last Name")

    email = models.EmailField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()

    def __str__(self):
        return self.email