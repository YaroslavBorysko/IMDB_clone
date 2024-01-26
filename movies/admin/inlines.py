from django.contrib import admin

from movies.models import Review, Comment, Movie


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class ActorInline(admin.TabularInline):
    model = Movie.actors.through
    extra = 0


class MovieInline(admin.TabularInline):
    model = Movie
    extra = 0
    fields = ("title", "release_year", "poster_image")
