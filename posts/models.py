"""Post models"""

from django.db import models


class User(models.Model):
    """User Model"""

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=80)

    full_name = models.CharField(max_length=80)
    bio = models.TextField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    country = models.CharField(max_length=80, default=None, blank=True, null=True)
    city = models.CharField(max_length=80, default=None, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)


    def __str__(self) -> str:
        """Return email"""
        return self.email
