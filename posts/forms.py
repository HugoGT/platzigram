"""Post forms"""


from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    """Post model form"""

    class Meta:
        """Form settings"""
        model = Post
        fields = ('user', 'profile', 'title', 'photo')
        exclude = ('user', 'profile')


class CommentForm(forms.ModelForm):
    """Comment model form"""

    class Meta:
        """Comment Settings"""
        model = Comment
        fields = ('user', 'post', 'comment')
        exclude = ('user',)