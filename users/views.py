"""Users views"""


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView

from .forms import ProfileForm, SignupForm
from posts.models import Post


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view"""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')

        return context


def signup_view(request):
    """Sign up view."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name='users/signup.html',
        context={
            'form': form,
        }
    )


def login_view(request):
    """Login view"""
    if request.user.is_authenticated:
        return redirect('posts:feed')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('users:login')


@login_required
def update_profile(request):
    """Update a user's profile view"""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            try:
                profile.phone_number = data['phone_number']
                profile.website = data['website']
                profile.biography = data['biography']
                profile.picture = data['picture']
                profile.save()

            except IntegrityError:
                return render(request, 'users/update_profile.html', {'error': 'This phone number is already in use'})

            messages.success(request, 'Your profile has been updated!')

            url = reverse('users:user_detail', kwargs={'username': request.user.username,})
            return redirect(url)

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile':profile,
            'user': request.user,
            'form': form,
        }
    )
