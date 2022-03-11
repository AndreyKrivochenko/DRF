from django.db import models
from django.contrib.auth.models import AbstractUser


class BackUser(AbstractUser):
    email = models.EmailField(unique=True)
