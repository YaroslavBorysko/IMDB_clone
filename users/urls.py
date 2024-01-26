from django.urls import path
from django.contrib.auth import views as auth_views

from users import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.edit_profile, name='profile'),
]