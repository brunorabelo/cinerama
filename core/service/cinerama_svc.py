import requests
import commons.constants
import json
from core.models import Movie, Rating, MovieWithRating
from django.core import serializers
from django.contrib.auth.models import User
import core.service.themoviedb_svc as themoviedb_api
  

# Retorna um json com as informaçoes do rating (movie_id, user e rating_value)
def save_rating(logged_user,rating_info):   
    user_rating = rating_info['user_rating']
    movie_id = rating_info['movie_id']


    movie, created = Movie.objects.get_or_create(tmdb_id = movie_id)
    rating, created = Rating.objects.get_or_create(user=logged_user, movie = movie)

    rating.rating_value = user_rating

    rating.save()

    return rating.model_to_json()


def get_movie_details(logged_user,movie_id):

    movie, created = Movie.objects.get_or_create(tmdb_id = movie_id)

    if created or (not movie.is_updated):
        movie.update_from_internet()

    movieWithRating = MovieWithRating(movie,logged_user)

    return movieWithRating.model_to_json()


def get_user_movie_list(user):

    ratings = Rating.objects.filter(user=user).exclude(rating_value__isnull=True).select_related('movie')
    movies = {'movies':[]}

    for rating in ratings:
        movieWithRating = MovieWithRating(rating.movie,user)
        movies['movies'].append(movieWithRating.model_to_json())
            

    return movies

def search_movies(movie_search):
    movies_json = themoviedb_api.get_search_json_results_from_api(movie_search)

    return movies_json


def list_movies_now_playing():
    movies_json = themoviedb_api.get_movies_json_now_playing_from_api()

    return movies_json




    



