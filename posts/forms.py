"""Post forms"""


from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    """Post model form"""

    class Meta:
        """Form settings"""
        model = Post
        fields = ('user', 'profile', 'title', 'photo')
