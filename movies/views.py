import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
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
