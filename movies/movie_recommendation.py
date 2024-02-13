from imdb import IMDb
import openai
from decouple import config

openai.api_key = config('OPENAI_API_KEY')


class MovieRecommendation:

    def __init__(
            self, genre, start_date, end_date, description
    ):
        self.genre = genre
        self.start_date = start_date
        self.end_date = end_date
        self.description = description

    def handle_ai_request(self):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    'role': 'user',
                    'content': f'Provide me with a movie recommendation. '
                               f'The movie should be in the {self.genre} genre '
                               f'and should be filmed in the datetime range between {self.start_date} and {self.end_date}. '
                               f'Additional description: {self.description}'
                },
                {
                    'role': 'user',
                    'content': 'Provide your response only with the only one  movie name without any other information'
                },
            ]
        )
        return response['choices'][0]['message']['content']

    @staticmethod
    def handle_imdb_request(movie_name):
        ia = IMDb()

        movies = ia.search_movie(movie_name)

        if not movies:
            return {}

        first_movie = ia.get_movie(movies[0].movieID)
        movie_details = {
            'title': first_movie.get('title'),
            'plot': first_movie.get('plot outline'),
            'release_year': first_movie.get('year'),
            'poster_url': first_movie.get('cover url')
        }

        return movie_details

    def handle(self):
        movie_name = self.handle_ai_request()
        return self.handle_imdb_request(movie_name)

