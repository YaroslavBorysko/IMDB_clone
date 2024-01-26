from django.shortcuts import render
from movies.models import Movie
from django.shortcuts import get_object_or_404


def movies_list(request):

    movies = Movie.objects.all()
    return render(
        request, 'movies/movies_list.html',
        context={'movies': movies}
    )


def movie_details(request, pk):

    movie = get_object_or_404(Movie, pk=pk)
    return render(
        request, 'movies/movie_detail.html',
        context={'movie': movie}
    )
