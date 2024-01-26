from django.contrib import admin

from movies.models import Movie, Review, Comment


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

