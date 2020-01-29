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
        

    # Testa avaliação, reavaliação, não avaliação e listagem dos filmes de um usuário
    def test_cinerama_api(self):
        jon = Client()
        jon.force_login(User.objects.get(username='jon'))

        # Testando avaliação de um filme
        movie_id=155 #batman
        rating_info = {
            "movie_id":movie_id,
        "rating":4.5}
        self._save_rating(jon,rating_info)

        self._assert_rating_user(jon,movie_id,4.5)

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

        self._assert_rating_user(jon,movie_id,2.0)

        
        # Testando filme não avaliado
        movie_id =265195 # relatos selvagen
        self._assert_filme_nao_avaliado(jon,movie_id)



        # testando lista de filmes
        user_movie_list= self._get_user_movie_list(jon,jon)


        self.assertEquals(len(user_movie_list),2)
        
        expectedResult = [{
                  'id': 155,
                  'title': "Batman: O Cavaleiro das Trevas",
                  'poster_path': "http://image.tmdb.org/t/p/original/kG5moUJwvIAW0w4JmnJJLu9cH9u.jpg",
                  'backdrop_path': "http://image.tmdb.org/t/p/original/xfKot7lqaiW4XpL5TtDlVBA9ei9.jpg",
                  'overview': "Após dois anos desde o surgimento do Batman, os criminosos de Gotham City têm muito o que temer. Com a ajuda do tenente James Gordon e do promotor público Harvey Dent, Batman luta contra o crime organizado. Acuados com o combate, os chefes do crime aceitam a proposta feita pelo Coringa e o contratam para combater o Homem-Morcego.",
                    'release_date':  "2008-07-16",

                  'user_rating': 3.5,

                },
                
                {
                  'id': 598,
                  'title': "Cidade de Deus",
                'overview': "Buscapé (Alexandre Rodrigues) é um jovem pobre, negro e muito sensível, que cresce em um universo de muita violência. Buscapé vive na Cidade de Deus, favela carioca conhecida por ser um dos locais mais violentos da cidade. Amedrontado com a possibilidade de se tornar um bandido, Buscapé acaba sendo salvo de seu destino por causa de seu talento como fotógrafo, o qual permite que siga carreira na profissão. É através de seu olhar atrás da câmera que Buscapé analisa o dia-a-dia da favela onde vive, onde a violência aparenta ser infinita.",
                  'release_date':  "2002-02-05",

                  'poster_path': "http://image.tmdb.org/t/p/original/pA70WUs7KHiHltfiBN4XEELOXcS.jpg",
                  'backdrop_path': "http://image.tmdb.org/t/p/original/k4BAPrE5WkNLvpsPsiMfu8W4Zyi.jpg",

                  'user_rating': 5.0,

                },
                ]

        expectedTitles = [t['title'] for t in expectedResult]
        expectedRatings = [t['user_rating'] for t in expectedResult]

        actualTitles = [t['title'] for t in user_movie_list]
        actualRatings = [t['user_rating'] for t in user_movie_list]

        self.assertEquals(expectedTitles,actualTitles)
        self.assertEquals(expectedRatings,actualRatings)
        
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
        

    def _get_user_movie_list(self,client,user):
        r = client.get('/api/get_movie_list',{'user':user})
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
