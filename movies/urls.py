from django.urls import path

from movies import views

urlpatterns = [
    path('', views.movies_list, name='movies_list')
]