from django.test import TestCase, Client
from django.urls import reverse

from .models import *


client = Client()


class TestMovieList(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name="New cat1")
        actor = Actor.objects.create(name="New actor")
        genre = Genre.objects.create(name="New genre")
        # movie_shots = MovieShots.objects.create(title="New movie shots")
        # rating_star = RatingStar.objects.create(title="New rating star")
        rating = Rating.objects.create(ip="127.0.0.1", movie_id=1, star_id=1)
        # review = Review.objects.create(ip="New review")
        self.movie = Movie.objects.create(
            title="New movie1",
            category=self.category,
            actor=actor,
            genre=genre,
            # movie_shots=movie_shots,
            rating_star=rating_star,
            rating=rating,
            review=review
        )

        self.new_movie_data = {
            "title": "new movie2",
            "category": self.category.id,
            "actor": actor.id,
            "genre": genre,
            # "movie_shots": movie_shots,
            "rating_star": rating_star,
            "rating": rating,
            "review": review
        }

    def test_movie_list(self):
        url = reverse("movie_list_create")
        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["results"][0]["title"], self.movie.title)
    #
    # def test_product_create(self):
    #     url = reverse("products_list_create")
    #
    #     response = client.post(url, data=self.new_product_data)
    #
    #     self.assertEqual(response.status_code, 201)
    #     self.assertNotEqual(response.status_code, 400)
    #     self.assertEqual(response.data["title"], self.new_product_data["title"])
    #
    # def test_product_detail(self):
    #     url = reverse("product_detail", kwargs={"slug": self.product.slug})
    #
    #     response = client.get(url)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(self.product.title, "New product1")
    #
    # def test_product_update(self):
    #     url = reverse("product_detail", kwargs={"slug": self.product.slug})
    #     data = {
    #         "title": "string",
    #         "price": 3000,
    #         "category": self.category.id
    #     }
    #
    #     response = client.put(url, data=data, content_type="application/json")
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data["title"], data["title"])
    #
    # def test_product_delete(self):
    #     url = reverse("product_detail", kwargs={"slug": self.product.slug})
    #
    #     response = client.delete(url)
    #
    #     self.assertEqual(response.status_code, 204)
    #     # self.assertEqual()
