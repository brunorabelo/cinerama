from django.db import models
from django.contrib.auth.models import User
import commons
import requests
import core.service.themoviedb_svc as movie_api

class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser")
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )

class Movie(models.Model):

    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200,null=True,blank=True)
    overview = models.TextField(null=True,blank=True)
    release_date = models.DateField(null=True,blank=True)
    backdrop_path = models.URLField(null=True,blank=True)
    poster_path = models.URLField(null=True,blank=True)

    @property
    def is_updated(self):
        if(self.title or self.overview or self.release_date or self.backdrop_path or self.poster_path):
            return False
        else: return True
    
    def update_from_internet(self):
        json = movie_api.get_updated_json_from_api(self)
        self.update_model_from_json(json)

    


    def update_model_from_json(self,json):
        movie = self
        movie.title = json['title']
        movie.overview = json['overview']
        movie.backdrop_path = json['backdrop_path']
        movie.poster_path = json['poster_path']
        
        movie.release_date = json['release_date']

        movie.save()

    def model_to_json(self):
        json = {}
        json['title'] = self.title 
        json['overview']= self.overview 
        json['id']=int(self.tmdb_id) 
        json['backdrop_path']=self.backdrop_path 
        json['poster_path']=self.poster_path 
        json['release_date']=self.release_date 

        return json

    def __str__(self):
        return "tmdb_id: {0} ({1})".format(self.tmdb_id,self.title or "Nõo atulizado")
    
    
    
class Rating(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    rating_value = models.FloatField(blank=True,null=True)
    
    def model_to_json(self):
        json = {}
        json['rating'] = self.rating_value
        json['movie_id']= self.movie.tmdb_id 
        json['username']= self.user.username 
        
        return json


    def __str__(self):
        return "user: {0} tmdb_id: {1} ({2})".format(self.user.username,self.movie.tmdb_id,self.movie.title or "Nõo atulizado")
    
class MovieWithRating:

    def __init__(self,movie,user):
        self.movie = movie
        self.user = user
        self.rating_value = self._getRating(movie,user)

    def _getRating(self,movie,user):

        if not user:
            return None

        rating,created = Rating.objects.get_or_create(user=user, movie = movie)
        
        return rating.rating_value
    
    def model_to_json(self):
        movie_json = self.movie.model_to_json()
        movie_json['user_rating'] = self.rating_value

        return movie_json