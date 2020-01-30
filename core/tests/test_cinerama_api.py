from core.models import User
from django.test.client import Client
from django.test.testcases import TestCase
from core.tests import fixtures
import json
import requests
from unittest.mock import Mock,patch

class TestCineramaApi(TestCase):

    @classmethod
    def setUpTestData(cls):
        fixtures.user_jon()
        fixtures.user_mary()
        
        
  

    def test_avaliacao_filme(self):
        jon = Client()
        jon.force_login(User.objects.get(username='jon'))

        # Testando avaliação de um filme
        movie_id=155 #batman
        rating_info = {
            "movie_id":movie_id,
            "rating":4.5}
        self._save_rating(jon,rating_info)

        self._assert_rating_user(jon,movie_id,4.5)

    def test_reavaliacao_filme(self):
        jon = Client()
        jon.force_login(User.objects.get(username='jon'))

        # Testando reavaliação de um filme
        movie_id=598 # cidade de deus
        rating_info = {
            "movie_id":movie_id,
        "rating":3.0}
        self._save_rating(jon,rating_info)

        self._assert_rating_user(jon,movie_id,3.0)

        movie_id=598 #cidade de deus
        rating_info = {
            "movie_id":movie_id,
        "rating":5.0}

        self._save_rating(jon,rating_info)

        self._assert_rating_user(jon,movie_id,5.0)
        
    def test_filme_nao_avaliado(self):
        jon = Client()
        jon.force_login(User.objects.get(username='jon'))
        # Testando filme não avaliado
        movie_id =265195 # relatos selvagen
        self._assert_filme_nao_avaliado(jon,movie_id)

    def test_user_movie_list(self):
        mary = Client()
        mary.force_login(User.objects.get(username='mary'))

        movie_id=155 #batman
        rating_info = {
            "movie_id":movie_id,
        "rating":1.5}
        self._save_rating(mary,rating_info)

        movie_id=598 # cidade de deus
        rating_info = {
            "movie_id":movie_id,
        "rating":5.0}
        self._save_rating(mary,rating_info)


        movie_id=598 #cidade de deus
        rating_info = {
            "movie_id":movie_id,
        "rating":1}

        self._save_rating(mary,rating_info)
        
        # Testando filme não avaliado
        movie_id =265195 # relatos selvagen
        self._assert_filme_nao_avaliado(mary,movie_id)

        # testando lista de filmes
        user_movie_list= self._get_user_movie_list(mary,'mary')

        #self.assertEquals(len(user_movie_list['movies']),2)
        
        expectedResult = {'movies':[{
                  'id': 155,
                  'title': None,
                  'poster_path': None,
                  'backdrop_path': None,
                  'overview': None,
                  'release_date':  None,

                  'user_rating': 1.5,

                },
                
                {
                  'id': 598,
                  'title': None,
                'overview': None,
                'release_date':  None,

                  'poster_path': None,
                  'backdrop_path': None,

                  'user_rating': 1.0,

                },
                ]
        }
        self.assertDictEqual(expectedResult,user_movie_list)


    @patch('core.service.cinerama_svc.requests.get')
    def test_user_movie_detail(self,mock_get):
        json_data = open('core/tests/assets/sample_movie.json')   
        movie_detail_json = json.load(json_data)
        json_data.close()

        mock_get.return_value=Mock(ok=True)
        mock_get.return_value.json.return_value=movie_detail_json


        mary = Client()
        mary.force_login(User.objects.get(username='mary'))
        r = mary.get('/api/get_movie_details',{'movie_id':645})

        self.assertEquals(200,r.status_code)

        data = json.loads(r.content.decode('utf-8'))
        expected_result = {
            
            'title': "007 Contra Octopussy",
            "overview": "Ao tentar solucionar quem assassinou o agente 009 (Andy Bradford), James Bond (Roger Moore) resolve seguir uma pista de uma jóia Fabergé roubada do Kremlin, que aparece em uma famosa casa de leilões de Londres. O agente 007 acredita que esta jóia pode ser a chave para solucionar o mistério, pois o agente morto foi encontrado com um Fabergé falso.",
            'id':645,
            'backdrop_path': "http://image.tmdb.org/t/p/original/nOp4RM4AYlW8Ux0XHBTqXbPlSgY.jpg",
            'poster_path': "http://image.tmdb.org/t/p/original/jebWDEnGH2f4GnqZxSLfuON5KME.jpg" ,
            'release_date': "1983-06-05",
            'user_rating': None,
    
        }


        self.assertDictEqual(expected_result,data)


    @patch('core.service.cinerama_svc.requests.get')
    def test_anon_movie_detail(self,mock_get):
        json_data = open('core/tests/assets/sample_movie.json')   
        movie_detail_json = json.load(json_data)
        json_data.close()

        mock_get.return_value=Mock(ok=True)
        mock_get.return_value.json.return_value=movie_detail_json


        client = Client()
        r = client.get('/api/get_movie_details',{'movie_id':645})

        self.assertEquals(200,r.status_code)

        data = json.loads(r.content.decode('utf-8'))
        expected_result = {
            
            'title': "007 Contra Octopussy",
            "overview": "Ao tentar solucionar quem assassinou o agente 009 (Andy Bradford), James Bond (Roger Moore) resolve seguir uma pista de uma jóia Fabergé roubada do Kremlin, que aparece em uma famosa casa de leilões de Londres. O agente 007 acredita que esta jóia pode ser a chave para solucionar o mistério, pois o agente morto foi encontrado com um Fabergé falso.",
            'id':645,
            'backdrop_path': "http://image.tmdb.org/t/p/original/nOp4RM4AYlW8Ux0XHBTqXbPlSgY.jpg",
            'poster_path': "http://image.tmdb.org/t/p/original/jebWDEnGH2f4GnqZxSLfuON5KME.jpg" ,
            'release_date': "1983-06-05",
            'user_rating': None,
    
        }


        self.assertDictEqual(expected_result,data)

        
        


    # Testa pesquisa de filmes
    @patch('core.service.cinerama_svc.requests.get')
    def test_search_movies(self,mock_get):
        movie_name ='pulp fiction'
        json_data = open('core/tests/assets/movie_search.json')   
        search_movies = json.load(json_data)
        json_data.close()

        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = search_movies

        client = Client()
        r = client.get('/api/get_movies_search_result',{'movie_search':movie_name})
        self.assertEquals(200,r.status_code)

        data = json.loads(r.content.decode('utf-8'))

        search_movies = {'movies':search_movies['results']}

        expectedIds = [t['id'] for t in search_movies["movies"]]
        actualIds = [t['id'] for t in data["movies"]]
        self.assertEquals(expectedIds,actualIds)

    # Testa filmes passando agora
    @patch('core.service.cinerama_svc.requests.get')
    def test_list_movies_now_playing(self,mock_get):
        json_data = open('core/tests/assets/movies_now_playing.json')   
        movies_now_playing_result = json.load(json_data)
        json_data.close()

        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = movies_now_playing_result

        client = Client()
        r = client.get('/api/list_movies_now_playing')
        self.assertEquals(200,r.status_code)

        data = json.loads(r.content.decode('utf-8'))

        movies_now_playing = {'movies':movies_now_playing_result['results']}


        expectedIds = [t['id'] for t in movies_now_playing["movies"]]
        actualIds = [t['id'] for t in data["movies"]]
        self.assertEquals(expectedIds,actualIds)

    def _save_rating(self,client,rating_info):
        r = client.post("/api/save_rating", {'rating_info':  json.dumps(rating_info),}) 
        self.assertEquals(200,r.status_code)
        data = json.loads(r.content.decode('utf-8'))
        self.assertIsNotNone(data)


    def _assert_rating_user(self,client,movie_id,rating):
        r = client.get('/api/get_movie_details',{'movie_id': movie_id ,})
        self.assertEquals(200,r.status_code)
        data = json.loads(r.content.decode('utf-8'))
        self.assertIsNotNone(data)

        self.assertIn('user_rating',data)
        self.assertEquals(data['user_rating'],rating)
        
    def _get_user_movie_list(self,client,username):
        r = client.get('/api/get_movie_list',{'username':username})
        self.assertEquals(200,r.status_code)
        data = json.loads(r.content.decode('utf-8'))
        self.assertIsNotNone(data)

        return data

    def _assert_filme_nao_avaliado(self,client,movie_id):
        r = client.get('/api/get_movie_details',{'movie_id': movie_id ,})
        self.assertEquals(200,r.status_code)
        data = json.loads(r.content.decode('utf-8'))
        self.assertIsNotNone(data)

        self.assertIn('user_rating',data)
        self.assertIsNone(data['user_rating'])
