"""Users views"""


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect

from .models import Profile


def signup_view(request):
    """Sign up a user"""
    if request.user.is_authenticated:
        return redirect('feed')

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_conf = request.POST['password_confirmation']

        if password_conf != password:
            return render(request, 'users/signup.html', {'error': 'Passwords do NOT match!, try again.'})

        else:
            try:
                validate_email(email)
                if User.objects.filter(email=email):
                    raise IntegrityError
            except ValidationError as e:
                return render(request, 'users/signup.html', {'error': e.message})
            except IntegrityError:
                return render(request, 'users/signup.html', {'error': 'Email has already been taken.'})
            else:
                try:
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        password=password,
                        email=email)
                except IntegrityError:
                    return render(request, 'users/signup.html', {'error': 'Username has already been taken.'})

                profile = Profile(user=user,)
                profile.save()

                return redirect('login')

    return render(request, 'users/signup.html')


def login_view(request):
    """Login view"""
    if request.user.is_authenticated:
        return redirect('feed')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password.'})

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('login')


@login_required
def update_profile(request):
    """Update a user's profile view"""
    return render(request, 'users/update_profile.html')