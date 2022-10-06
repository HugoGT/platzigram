"""User Forms"""


from django import forms


class ProfileForm(forms.Form):
    """Profile form"""

    picture = forms.ImageField(required=False)
    website = forms.URLField(max_length=160, required=False)
    biography = forms.CharField(max_length=600, required=True)
    phone_number = forms.CharField(max_length=20, required=False)