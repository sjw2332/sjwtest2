import requests
from movie_model import MovieModel


url = '''
https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number=1&limit=20
'''


def callMovieApi():
    response = requests.get(url)
    responseDic = response.json()
    movies = responseDic["data"]["movies"]

    return convert_model(movies)

def convert_model(movies):
    movieList = []

    for movie in movies:
        movie_model = MovieModel(movie["title"],movie["rating"],movie["summary"],movie["small_cover_image"])
        movieList.append(movie_model)
    print(type(movie["title"]))
    print(type(movie["rating"]))
    print(type(movie["summary"]))
    print(type(movie["small_cover_image"]))
    return movieList


