from django.urls import path, include
from django.contrib import admin

from .views import hello_world, numbers, hi

from posts import views as posts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome', hello_world),
    path('numbers', numbers),
    path('hi/<str:name>/<int:age>', hi),

    path('', posts_views.list_posts),
]
