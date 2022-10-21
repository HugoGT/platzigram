"""User Forms"""


from django import forms
from django.contrib.auth.models import User

from .models import Profile


class ProfileForm(forms.ModelForm):
    """Profile form"""

    class Meta:
        model = Profile
        fields = ('website', 'biography', 'phone_number', 'picture')


class SignupForm(forms.Form):
    """Sign up form"""
    username = forms.CharField(
        label=False,
        min_length=2,
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control',
                }
            )
        )

    first_name = forms.CharField(
        label=False, min_length=2,
        max_length=60,
        widget = forms.TextInput(
            attrs={
                'placeholder':'First name',
                'class': 'form-control',
                }
            )
        )

    last_name = forms.CharField(
        label=False,
        min_length=2,
        max_length=60,
        widget = forms.TextInput(
            attrs={
                'placeholder':'Last name',
                'class': 'form-control',
                }
            )
        )

    email = forms.EmailField(
        label=False,
        min_length=6,
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Email',
                'class': 'form-control',
                }
            )
        )

    password = forms.CharField(
        label=False,
        max_length=80,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class': 'form-control',
                }
            )
        )

    password_confirmation = forms.CharField(
        label=False,
        max_length=80,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password confirmation',
                'class': 'form-control',
                }
            )
        )

    def clean_username(self):
        """Username must be unique"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')

        return username

    def clean_password(self):
        """Verify password confirmation match"""

        password = self.data['password']
        password_confirmation = self.data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')
        if len(password) < 6:
            raise forms.ValidationError('Password must contain 6 or more characters.')

        return password

    def save(self):
        """Create user and profile"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile.objects.create(user=user)
        profile.save()
