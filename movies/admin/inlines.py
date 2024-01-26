from django.contrib import admin

from movies.models import Review, Comment, Movie


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class ActorInline(admin.TabularInline):
    model = Movie.actors.through
    extra = 1

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"


# class DirectorInline(admin.StackedInline):
#     model = Movie
#     fk_name = "director"
#     extra = 1
#
#     class Meta:
#         verbose_name = "Director"
#         verbose_name_plural = "Directors"
