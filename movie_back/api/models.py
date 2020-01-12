from django.db import models
from django.conf import settings
# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=150)

class Actor(models.Model):
    name = models.CharField(max_length=100)

class Director(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    movieCd = models.IntegerField()
    title = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)
    summary = models.TextField()
    poster_url = models.TextField()
    trailer_url = models.TextField()
    opendt = models.DateField()
    naver_score = models.FloatField()
    grade = models.CharField(max_length=50)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked_movies')
    genres = models.ManyToManyField(Genre, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    directors = models.ManyToManyField(Director, related_name='movies')

class Rating(models.Model):
    comment = models.TextField()
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, related_name='ratings', on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    movietitle = models.CharField(max_length=50)
    