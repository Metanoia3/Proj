from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import MovieViewSet, RatingViewSet, UserMovieViewSet

# Create a router and register our viewset with it
router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)
router.register('users', UserMovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
