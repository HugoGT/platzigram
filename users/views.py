"""Users views"""


from django.contrib import messages
from django.contrib.auth import authenticate, login, views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView

from .forms import ProfileForm, SignupForm
from .models import Relationship
from posts.models import Post


class SignupView(FormView):
    """Sign up view"""
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:update_profile')

    def form_valid(self, form):
        form.save()

        username = form['username'].value()
        password = form['password'].value()

        user = authenticate(self.request, username=username, password=password)

        login(self.request, user)

        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    """Login view"""
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    """Logout a user"""
    pass


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
        posts = Post.objects.filter(user=user)
        context['posts'] = posts.order_by('-created')
        context['count_posts'] = posts.count()

        return context


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view"""
    template_name = 'users/update_profile.html'
    form_class = ProfileForm

    def get_object(self):
        """Return to user's profile"""
        return self.request.user.profile

    def get_success_url(self):
        username = self.request.user.username
        return reverse('users:user_detail', kwargs={'username': username,})


@login_required
def follow(request, username):
    current_user = request.user
    to_user = get_object_or_404(User,username=username)
    relation = Relationship(from_user=current_user, to_user=to_user)
    relation.save()
    messages.success(request, f'You are following {username}')

    return redirect(reverse('users:user_detail', kwargs={'username':username,}))


@login_required
def unfollow(request, username):
    current_user = request.user
    to_user = get_object_or_404(User,username=username)
    relation = Relationship.objects.filter(from_user=current_user.id, to_user= to_user.id).get()
    relation.delete()
    messages.success(request, f'You unfollow {username}')

    return redirect(reverse('users:user_detail', kwargs={'username':username,}))
