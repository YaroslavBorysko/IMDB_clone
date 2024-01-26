from django.shortcuts import render
from movies.models import Movie


def movies_list(request):

    movies = Movie.objects.all()
    return render(
        request, 'movies/movies_list.html',
        context={'movies': movies}
    )
