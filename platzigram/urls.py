"""URLs module"""


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    #Users views
    path('', include(('users.urls', 'users'), namespace='users')),

    #Post views
    path('', include(('posts.urls', 'posts'), namespace='posts')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
