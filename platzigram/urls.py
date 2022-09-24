"""URLs module"""


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts import views as posts_views
from .views import hello_world, numbers, hi


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome', hello_world),
    path('numbers', numbers),
    path('hi/<str:name>/<int:age>', hi),

    path('', posts_views.list_posts),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
