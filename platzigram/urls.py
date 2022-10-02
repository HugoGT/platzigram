"""URLs module"""


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts import views as posts_views
from users import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),

    #Post views
    path('', posts_views.list_posts, name='feed'),

    #Users views
    path('login/', users_views.login_view, name='login'),
    path('logout/', users_views.logout_view, name='logout'),
    path('signup/', users_views.signup_view, name='signup'),
    path('me/profile/', users_views.update_profile, name='update_profile')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
