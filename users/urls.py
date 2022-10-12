"""Users URLs"""


from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),

    path('profile/', views.update_profile, name='update_profile'),
    path('profile/<str:username>/', views.UserDetailView.as_view(), name='user_detail'),
]
