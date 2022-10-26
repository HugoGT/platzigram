"""Post models"""


from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    """Post model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts')
    likes = models.ManyToManyField(User, related_name='post_likes')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns the title and username"""
        return f'{self.title} by @{self.user.username}'

    def count_likes(self):
        """Returns the amount of likes of the post"""
        return self.likes.count()

    def get_absolute_url(self):
        """Returns the url of the post"""
        return reverse('posts:post_detail', kwargs={'id': self.post.id})


class Comment(models.Model):
    """Comments model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    comment = models.CharField(max_length=600)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns the comment"""
        return f'{self.comment}'

    def get_absolute_url(self):
        """Returns the url of the post"""
        return reverse('posts:post_detail', kwargs={'id': self.post.id})
