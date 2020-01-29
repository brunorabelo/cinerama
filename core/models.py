from django.db import models
from django.contrib.auth.models import User

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

    tmdb_id = models.IntegerField()
    title = models.CharField(max_length=200,null=True,blank=True)
    overview = models.TextField(null=True,blank=True)
    release_date = models.DateField(null=True,blank=True)
    backdrop_path = models.URLField(null=True,blank=True)
    poster_path = models.URLField(null=True,blank=True)

    user_ratings = models.ManyToManyField(User)

