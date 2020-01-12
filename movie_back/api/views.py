from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Genre, Movie, Rating, Actor
from .serializers import GenreSerializer, MovieDetailSerializer, MovieSerializer, RatingSerializer
from accounts.models import User
from rest_framework.permissions import AllowAny 
from rest_framework import serializers


@api_view(['GET'])
@permission_classes([AllowAny])
def movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def genres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def rating_delete(request, rating_id):
    rating = get_object_or_404(Rating, pk=int(rating_id))
    print(rating.id)
    rating.delete()
    return Response('Complete Delete')


@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def rating_add(request):
    comment = request.data.get('comment')
    score = int(request.data.get('score'))
    user_id = request.data.get('user_id')
    movie_id = request.data.get('movie_id')
    rating = Rating()
    rating.comment = comment
    rating.score = score
    user = User.objects.get(pk=user_id)
    rating.user = user
    movie = Movie.objects.get(pk=movie_id)
    rating.movie = movie
    rating.movietitle = movie.title
    rating.username = user.username
    rating.save()
    serializer = RatingSerializer(instance=rating)
    # print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def unlike_like(request, movie_id, user_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = get_object_or_404(User, pk=user_id)
    if user in movie.liked_users.all():
        movie.liked_users.remove(user)
    else:
        movie.liked_users.add(user)
    return Response('Success')


@api_view(['GET'])
def get_rating(request, rating_id):
    rating = get_object_or_404(Rating, pk=rating_id)
    serializer = RatingSerializer(rating)
    return Response(serializer.data)

def get_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(rating)
    return Response(serializer.data)