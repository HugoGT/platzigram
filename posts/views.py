"""Posts views"""


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import PostForm, CommentForm
from .models import Post, Comment


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts"""
    model = Post

    template_name = 'posts/feed.html'
    ordering = ('-created',)
    paginate_by = 20
    context_object_name = 'posts'


class PostsCreateView(LoginRequiredMixin, CreateView):
    """Create a new post"""

    template_name = 'posts/new_post.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.profile = self.request.user.profile
        messages.success(self.request, 'Your post has been created!')

        return super().form_valid(form)


class PostsDetailView(LoginRequiredMixin, DetailView):
    """Post detail view"""

    template_name = 'posts/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["comments"] = Comment.objects.filter(post=post).order_by('-created')

        return context


class PostCreateComment(LoginRequiredMixin, CreateView):
    """Create a comment in a post"""

    form_class = CommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


@login_required
def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user.id)

    return redirect('posts:post_detail', id = id)
