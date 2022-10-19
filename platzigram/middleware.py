"""Platzigram users middleware"""


from django.shortcuts import redirect
from django.urls import reverse

from . import settings


class ProfileCompletionMiddleware:
    """Profile completion middleware

    Ensure every user that is interacting with the platform have their profile picture and biography
    """

    def __init__(self, get_response):
        """Middleware initialization"""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be exectued for each request before the view is called"""
        if not request.user.is_anonymous:
            if not request.path.startswith(settings.MEDIA_URL):
                if not request.user.is_staff:
                    profile = request.user.profile
                    if not profile.biography:
                        if request.path != [reverse('users:logout'), reverse('users:update_profile')]:
                            return redirect('users:update_profile')

        response = self.get_response(request)
        return response
