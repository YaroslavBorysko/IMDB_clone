from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.functions import Coalesce

from movies.models.mixins import UserMovieMixin

CURRENT_YEAR = current_year = datetime.now().year


class Movie(models.Model):
    """
    Represents a movie in the database, capturing essential information such as title,
    plot, director, actors, release year and poster image.
    """
    title = models.CharField(max_length=150, verbose_name=_("movie title"))
    plot = models.TextField(max_length=5000, null=True, blank=True, verbose_name=_("plot"))
    actors = models.ManyToManyField("users.Actor", blank=True, verbose_name=_("actors"))
    director = models.ForeignKey(
        "users.Director", null=True, blank=True, on_delete=models.CASCADE, related_name='directed_movies'
    )
    release_year = models.IntegerField(
        validators=[MaxValueValidator(CURRENT_YEAR)], verbose_name=_("movie release year")
    )
    poster_image = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title

    @property
    def test(self):
        return "ss"

    @property
    def total_rating(self):
        avg_rating = self.review_set.aggregate(
            avg_sum_of_fields=Coalesce(models.Avg(
                'rating', output_field=models.FloatField()
            ), 0.0))["avg_sum_of_fields"]

        return avg_rating


class Review(UserMovieMixin):
    """
    Represents a movie review, encompassing details such as the reviewer's information,
    associated movie, rating, and optional comments.
    """
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name=_("movie rating")
    )
    text = models.TextField(max_length=5000, blank=True, verbose_name=_("text of review for movie"))

    class Meta:
        unique_together = ("user", "movie")

    def __str__(self):
        return f"{self.user.first_name} - {self.movie.title}"


class Comment(UserMovieMixin):
    """
    Represents a movie comment in the database, encompassing details and optional comments.
    """
    text = models.TextField(max_length=5000, blank=True, verbose_name=_("text"))

    def __str__(self):
        return f"{self.user.first_name} - {self.movie.title}"
