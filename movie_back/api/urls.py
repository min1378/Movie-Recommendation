
from django.urls import path, include
from . import views


app_name = 'api'

urlpatterns = [
    path('movies/', views.movies),
    path('movies/<int:movie_id>/', views.movie_detail),
    path('movies/rating_add/', views.rating_add),
    path('rating_delete/<int:rating_id>/', views.rating_delete),
    path('genres/', views.genres),
    path('ratings/<int:rating_id>/', views.get_rating),
    path('movies/<int:movie_id>/', views.get_movie),
    path('movies/<int:movie_id>/unlike_like/<int:user_id>/', views.unlike_like),
]