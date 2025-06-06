from rest_framework import serializers
from .models import Rating, Movie
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie  
        fields = ('id', 'title', 'description', 'no_of_ratings', 'avg_rating')
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
        }
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        token = Token.objects.create(user=user)
        return user


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'movie', 'user', 'stars')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')