from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import Actor, Director, BaseUser


class Movie(models.Model):
    """
    Model for a movie in the database.
    """
    movie_id = models.AutoField(primary_key=True, verbose_name=_("movie_id"))
    title = models.CharField(max_length=150, null=True, unique=False, verbose_name=_("movie_title"))
    plot = models.TextField(max_length=5000, blank=True, verbose_name=_("plot"))
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='directed_movies')
    actors = models.ManyToManyField(Actor)
    release_year = models.IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2024)],
                                       verbose_name=_("movie release year"))
    poster_image = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("movie")


class Review(models.Model):
    """
    Model for a review in the database.
    """
    review_id = models.AutoField(primary_key=True, verbose_name=_("movie_review_id"))
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],
                                 verbose_name=_("movie_rating"))
    comment = models.TextField(max_length=5000, blank=True, verbose_name=_("comment for movie"))

    def __str__(self):
        return f"{self.user.first_name} - {self.movie.title}"

    class Meta:
        verbose_name = _("review")


class Discussion(models.Model):
    """
        Model for a discussion in the database.
    """
    discussion_id = models.AutoField(primary_key=True, verbose_name=_("discussion_id"))
    topic = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("topic"))
    posts = models.ManyToManyField(BaseUser)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = _("discussion")


class Post(models.Model):
    """
        Model for a post in the database.
    """
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='posts')
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='discussion_posts')
    post_text = models.TextField(max_length=5000, blank=True, verbose_name=_("post text"))

    def __str__(self):
        return f"{self.user} - {self.post_text}"

    class Meta:
        verbose_name = _("post")
