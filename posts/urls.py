"""Posts URLs"""


from django.urls import path

from . import views


urlpatterns = [
    path('', views.PostsFeedView.as_view(), name='feed'),
    path('new-post', views.create_post, name='new_post'),
    path('post/<int:id>', views.PostDetailView.as_view(), name='post_detail'),
]