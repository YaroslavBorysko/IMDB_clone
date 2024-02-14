import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from movies.forms import CommentForm
from movies.models import Movie, Review, Comment
from users.models import BaseUser


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


def create_movie_review(request, pk):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=pk)
        json_data = json.loads(request.body.decode('utf-8'))
        rating = json_data.get('rating')
        text = json_data.get('text')
        user = get_object_or_404(BaseUser, pk=json_data.get('user_id'))
        Review.objects.create(
            movie=movie, rating=rating,
            text=text, user=user
        )

        return HttpResponse('Form submitted successfully')

    return render(request, 'movies/reviews.html')


def dashboard(request):
    comments = Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST, user=request.user)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = form.user
            instance.save()

        return redirect('dashboard')
    else:
        form = CommentForm()
    return render(
        request, 'movies/discussion_dashboard.html',
        {'form': form, 'comments': comments}
    )


def create_movie_recommendation(request):
    if request.method == 'POST':
        json_data = request.POST
        genre = json_data.get('genre')
        start_date = json_data.get('start_date')
        end_date = json_data.get('end_date')
        description = json_data.get('description')

        # movie = MovieRecommendation(
        #     genre=genre, start_date=start_date,
        #     end_date=end_date, description=description
        # )

        return JsonResponse({"title": "The Blair Witch Project",
                             "plot": " must have seen something. Could the nightmarish myth be real?",
                             "release_year": 1999,
                             "poster_url": "https://m.media-amazon.com/images/M/MV5BNzQ1NDBlNDItMDAyYS00YTI2LTgwMmYtMzAwMzg4NDFlM2ZmXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX101_CR0,0,101,150_.jpg"
})

    return render(request, 'movies/recommendation_form.html')
