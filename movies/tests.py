# from django.test import TestCase, Client
# from django.urls import reverse
#
# from .models import *
#
#
# client = Client()
#
#
# class TestMovieList(TestCase):
#     def setUp(self) -> None:
#         self.category = Category.objects.create(name="New cat1")
#         actor = Actor.objects.create(name="New actor")
#         genre = Genre.objects.create(name="New genre")
#         # movie_shots = MovieShots.objects.create(title="New movie shots")
#         # rating_star = RatingStar.objects.create(title="New rating star")
#         rating = Rating.objects.create(ip="127.0.0.1", movie_id=1, star_id=1)
#         # review = Review.objects.create(ip="New review")
#         self.movie = Movie.objects.create(
#             title="New movie1",
#             category=self.category,
#             actor=actor,
#             genre=genre,
#             # movie_shots=movie_shots,
#             rating_star=rating_star,
#             rating=rating,
#             review=review
#         )
#
#         self.new_movie_data = {
#             "title": "new movie2",
#             "category": self.category.id,
#             "actor": actor.id,
#             "genre": genre,
#             # "movie_shots": movie_shots,
#             "rating_star": rating_star,
#             "rating": rating,
#             "review": review
#         }
#
#     def test_movie_list(self):
#         url = reverse("movie_list_create")
#         response = client.get(url)
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json()["results"][0]["title"], self.movie.title)