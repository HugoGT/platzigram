"""Post models"""


from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    """Post model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/pictures')
    likes = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username"""
        return f'{self.title} by @{self.user.username}'


class Comment(models.Model):
    """Comments model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    comment = models.CharField(max_length=600)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return comment and username"""
        return f'{self.comment}   -{self.user.username}'

    def get_absolute_url(self):
        return reverse('posts:post_detail', kwargs={'id': self.post.id})
