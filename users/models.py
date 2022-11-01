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

    picture = models.ImageField(upload_to='users', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns username"""
        return self.user.username

    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.user).values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)

    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self.user).values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)


class Relationship(models.Model):
    from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.from_user} is following {self.to_user}'
