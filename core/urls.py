from core import views
from django.conf.urls import url

urlpatterns = [
    url(r'^api/dapau$', views.dapau),
    url(r'^api/login$', views.login),
    url(r'^api/logout$', views.logout),
    url(r'^api/whoami$', views.whoami),

    url(r'^api/list_movies_now_playing',views.list_movies_now_playing),
    url(r'^api/save_rating$',views.save_rating),
    url(r'^api/get_movie_details',views.get_movie_details),
    url(r'^api/get_movie_list',views.get_movie_list),
    url(r'^api/get_movies_search_result',views.get_movies_search_result)
    
]
