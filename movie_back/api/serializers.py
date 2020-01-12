from rest_framework import serializers
from .models import Movie, Genre, Rating, Director, Actor
from accounts.serializers import UserSerializer
from accounts.models import User

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'comment', 'score', 'created_at', 'user', 'username', 'movietitle', 'movie']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name' ]


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name' ]


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    directors = DirectorSerializer(many=True)
    actors = ActorSerializer(many=True)
    liked_users = UserSerializer(many=True)
    ratings = RatingSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'naver_score', 'poster_url', 'opendt', 'genres', 'directors', 'actors', 'grade', 'ratings', 'liked_users']


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    directors = DirectorSerializer(many=True)
    actors = ActorSerializer(many=True)
    liked_users = UserSerializer(many=True)
    ratings = RatingSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'title_en', 'summary', 'naver_score', 'poster_url', 'trailer_url', 'opendt', 'genres', 'directors', 'actors', 'grade', 'liked_users', 'ratings']

