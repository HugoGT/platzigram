"""Posts URLs"""


from django.urls import path

from . import views


urlpatterns = [
    path('', views.PostsFeedView.as_view(), name='feed'),
    path('new-post', views.PostsCreateView.as_view(), name='new_post'),
    path('post/<int:id>', views.PostsDetailView.as_view(), name='post_detail'),
]