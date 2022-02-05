from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class User(AbstractUser):
    username = models.CharField(db_index=True, max_length=255, unique=True, default="")
    email = models.EmailField(db_index=True, unique=True, null=True, blank=True, default="")
    firstname = models.CharField(max_length=150, blank=True, default="")
    lastname = models.CharField(max_length=150, blank=True, default="")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.email}"
