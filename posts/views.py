"""Posts views"""


from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import PostForm
from .models import Post


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts"""
    model = Post

    template_name = 'posts/feed.html'
    ordering = ('-created',)
    paginate_by = 10
    context_object_name = 'posts'


class PostsDetailView(LoginRequiredMixin, DetailView):
    """Post detail view"""

    template_name = 'posts/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    queryset = Post.objects.all()


class PostsCreateView(LoginRequiredMixin, CreateView):
    """Create a new post"""

    template_name = 'posts/new_post.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)