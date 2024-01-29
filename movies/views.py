from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from movies.models import Movie
from django.shortcuts import get_object_or_404


def movies_list(request):
    movies_list = Movie.objects.all()
    items_per_page = 12
    paginator = Paginator(movies_list, items_per_page)

    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    return render(
        request, 'movies/movies_list.html',
        context={'movies': movies}
    )


def movie_details(request, pk):

    movie = get_object_or_404(Movie, pk=pk)
    is_user_reviewed = request.user in [
        review.user for review in
        movie.review_set.all()
    ]
    return render(
        request, 'movies/movie_detail.html',
        context={'movie': movie, 'is_reviewed': is_user_reviewed}
    )
