from django.urls import path
from django.contrib import admin

from .views import hello_world, numbers, hi


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome', hello_world),
    path('numbers', numbers),
    path('hi/<str:name>/<int:age>', hi),
]
