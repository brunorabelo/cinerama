# coding: utf-8
import json
from django.http.response import HttpResponse, JsonResponse
from django.contrib import auth
from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required
from core.service import log_svc, cinerama_svc
from django.views.decorators.csrf import csrf_exempt
from core.models import User


def dapau(request):
    raise Exception('break on purpose')


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != 'post':
        raise Exception('Logout only via post')
    if request.user.is_authenticated():
        log_svc.log_logout(request.user)
    auth.logout(request)
    return HttpResponse('{}', content_type='application/json')


def whoami(request):
    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    } if request.user.is_authenticated() else {'authenticated': False}
    return JsonResponse(i_am)


def list_movies_now_playing(request):
    data = cinerama_svc.list_movies_now_playing()
    return JsonResponse(data)


@ajax_login_required
def save_rating(request):
    rating_info = json.loads(request.POST['rating_info'])
    user = request.user
    data = cinerama_svc.save_rating(user,rating_info)
    return JsonResponse(data)

def get_movie_details(request):
    movie_id = request.GET['movie_id']
    user = request.user if request.user.is_authenticated() else None
    
    data = cinerama_svc.get_movie_details(user,movie_id)

    return JsonResponse(data)

@ajax_login_required
def get_movie_list(request):
    username = request.GET['user']
    #user = request.user

    user = User.objects.get(username=username)
    
    data = cinerama_svc.get_user_movie_list(user)

    return JsonResponse(data)

def get_movies_search_result(request):
    movie_search = request.GET['movie_search']

    data = cinerama_svc.search_movies(movie_search)

    return JsonResponse(data)


    


def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d
