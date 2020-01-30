import requests
import json
from commons.constants import API_KEY_MOVIE_DB

def get_updated_json_from_api(movie):
    api_key = API_KEY_MOVIE_DB
    url = "https://api.themoviedb.org/3/movie/{0}".format(movie.tmdb_id)

    params = {'api_key':api_key,'language':'pt-BR'}

    try:
    
        response = requests.get(url,params=params)

        data = response.json()

        movie = _clean_json_url_path(data)

    except requests.exceptions.RequestException as e:
        return _Empty_return.empty_json()


    return movie

def get_search_json_results_from_api(query):
    api_key = API_KEY_MOVIE_DB
    url = "https://api.themoviedb.org/3/search/movie"

    params = {'api_key':api_key,'language':'pt-BR','region':'BR','page':'1','query':query}

    try:
        response = requests.get(url,params=params)

        data = response.json()

        result = _clean_json_list_url_path(data['results'])


    except requests.exceptions.RequestException as e:
        return _Empty_return().empty_list()

        

    movies = {"movies":result}
    return movies

def get_movies_json_now_playing_from_api():

    api_key = API_KEY_MOVIE_DB
    url = "https://api.themoviedb.org/3/movie/now_playing"

    params = {'api_key':api_key,'language':'pt-BR','region':'BR','page':'1'}

    try:
        response = requests.get(url,params=params)

        data = response.json()

        result = _clean_json_list_url_path(data['results'])

    except requests.exceptions.RequestException as e:
        return _Empty_return().empty_list()

    movies = {"movies":result}
    return movies

def _clean_json_url_path(t):
    url_format = "http://image.tmdb.org/t/p/original"
    


    t['backdrop_path']="{0}{1}".format(url_format if t['backdrop_path'] else '', t['backdrop_path'] if t['backdrop_path'] else 'https://i.ya-webdesign.com/images/image-not-found-png.png') 
    t['poster_path']="{0}{1}".format(url_format if t['poster_path'] else '',t['poster_path'] if t['poster_path'] else 'https://i.ya-webdesign.com/images/image-not-found-png.png') 
    

    return t

def _clean_json_list_url_path(data):

    l = list(map(_clean_json_url_path,data))
    
    return l


class _Empty_return:
    def empty_list():
        return {"movies":[]}
    def empty_json():
        return {
            'title':'',
            'overview':'',
            'backdrop_path':'',
            'poster_path':'',
            'release_date':None,
            }

