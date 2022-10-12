"""Posts views"""


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import PostForm
from .models import Post


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts"""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 10
    context_object_name = 'posts'


@login_required
def create_post(request):
    """Create a new post"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been created!')

            return redirect('posts:feed')

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new_post.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile,
        }
    )
