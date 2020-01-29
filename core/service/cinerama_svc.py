import requests
import commons.constants
import json
def save_rating(user,rating_info):
    return []


def get_movie_details(user,movie_id):
    return []

def get_user_movie_list(user):
    return []

def search_movies(movie_search):
    
    api_key = commons.constants.API_KEY_MOVIE_DB
    url = "https://api.themoviedb.org/3/search/movie"

    params = {'api_key':api_key,'language':'pt-BR','region':'BR','page':'1','query':movie_search}

    response = requests.get(url,params=params)

    data = response.json()

    result = _convert_img_path_to_url(data['results'])

    movies = {"movies":result}
    return movies


def list_movies_now_playing():
    
    api_key = commons.constants.API_KEY_MOVIE_DB
    url = "https://api.themoviedb.org/3/movie/now_playing"

    params = {'api_key':api_key,'language':'pt-BR','region':'BR','page':'1'}


    #url = "https://api.themoviedb.org/3/movie/now_playing?api_key={0}&language={1}&page=1&region={2}".format(api_key,"pt-BR",'BR')

    response = requests.get(url,params=params)

    data = response.json()


    result = _convert_img_path_to_url(data['results'])

    movies = {"movies":result}
    return movies

def _convert_url(t):
    url_format = "http://image.tmdb.org/t/p/original"
    
    t['backdrop_path']="{0}{1}".format(url_format,t['backdrop_path']) 
    t['poster_path']="{0}{1}".format(url_format,t['poster_path']) 
    

    return t

def _convert_img_path_to_url(data):

    l = list(map(_convert_url,data))
    
    return l




    



