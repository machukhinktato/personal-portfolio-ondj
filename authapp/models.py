from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    github_link = models.URLField()
    is_active = models.BooleanField(default=False)
