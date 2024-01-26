from django.contrib import admin

from movies.admin import ReviewInline, CommentInline, ActorInline
from movies.models import Movie, Review, Comment


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'director', 'total_rating')
    search_fields = (
        'title', 'director__first_name', 'director__last_name', 'actor__first_name', 'actor__last_name'
    )
    list_filter = ('release_year',)
    inlines = [ReviewInline, CommentInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'rating', 'text')
    list_filter = ('rating',)
    search_fields = ('user__first_name', 'user__last_name', 'movie__title')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'text')
    search_fields = ('user__first_name', 'user__last_name', 'movie__title')
