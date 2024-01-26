from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from movies.models import Movie


def movies_list(request):
    movies_list = Movie.objects.all()
    items_per_page = 4
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
