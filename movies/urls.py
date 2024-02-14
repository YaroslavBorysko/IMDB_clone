from django.urls import path

from movies import views

urlpatterns = [
    path('', views.movies_list, name='movies_list'),
    path('movie/<int:pk>/', views.movie_details, name='movie_detail'),
    path('movie/<int:pk>/review-create/', views.create_movie_review, name='create_movie_review'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('recommendation/', views.create_movie_recommendation, name='recommendation'),
]