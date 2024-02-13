from django.core.management.base import BaseCommand
from imdb import IMDb
from movies.models import Movie
from django.core.files.base import ContentFile
import requests


class Command(BaseCommand):
    help = 'Import movies from IMDb'

    def handle(self, *args, **options):
        ia = IMDb()
        top_movies = ia.search_movie("the")[:20]
        movies_lst = []
        print("starting")

        for item in top_movies:
            movie = ia.get_movie(item.movieID)
            ia.update(movie, ['main'])

            title = movie.get('title')
            plot = movie.get('plot outline')
            release_year = movie.get('year')
            poster_url = movie.get('cover url')

            instance = Movie(
                title=title,
                plot=plot,
                release_year=release_year,
            )
            if poster_url:
                print("requesting photo")
                response = requests.get(poster_url)
                if response.status_code == 200:
                    file_name = f"{movie.movieID}_poster.jpg"
                    instance.poster_image.save(file_name, ContentFile(response.content), save=False)
            movies_lst.append(instance)
        print(f"Saving {len(movies_lst)} movies")
        Movie.objects.bulk_create(movies_lst)
        self.stdout.write(self.style.SUCCESS(f'Successfully imported'))

