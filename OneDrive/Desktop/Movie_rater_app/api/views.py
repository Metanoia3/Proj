from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Movie, Rating
from .serializer import MovieSerializer, RatingSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

# Create your views here.
class UserMovieViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            print('user:', user)
            #user = User.objects.get(id=1)
            #print('user:', user.username)
            
            try:
                rating = Rating.objects.get(user = user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many = False)
                response = {
                    'message': 'Rating updated successfully.', 'result': serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)

            except Rating.DoesNotExist:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingSerializer(rating, many = False)
                response = {
                    'message': 'Rating created.', 'result': serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
                
        else:
            response = {
                "message": "Stars field is required."
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, *args, **kwargs):
        response = {
            "message": "This endpoint is not allowed for movies."
        }
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def create(self, request, *args, **kwargs):
        response = {
            "message": "This endpoint is not allowed for movies."
        }
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
