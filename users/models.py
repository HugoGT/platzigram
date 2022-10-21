"""Users models"""


from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model

    Proxy model that extends the base data with other information
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=160, blank=True)
    biography = models.TextField(max_length=600, blank=True)
    phone_number = models.CharField(unique=True, max_length=16, blank=True, null=True)

    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns username"""
        return self.user.username