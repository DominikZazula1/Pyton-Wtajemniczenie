from datetime import date

from . import permissions, movies_directory
from .movie import Movie
from .rented_movie import RentedMovie
from .exceptions import (
    NoCreditsForMovieRent,
    ActionNotAllowed,
    MovieNotFound,
    ViewsLimitReached,
)


def rent_movie(user, movie):
    if user.credits_left < 1:
        raise NoCreditsForMovieRent()
    user.rented_movies.append(RentedMovie(movie))
    user.credits_left -= 1


def watch_movie(user, movie):
    def get_rented_movie(user_with_movies, searching_movie):
        for rented_movie in user_with_movies.rented_movies:
            if rented_movie.movie == searching_movie:
                return rented_movie

    user_rented_movie = get_rented_movie(user, movie)
    if not user_rented_movie:
        raise MovieNotFound()

    if user_rented_movie.views_left < 1:
        raise ViewsLimitReached()

    user_rented_movie.views_left -= 1
    _start_streaming(user, movie)


def _start_streaming(user, movie):
    print(f"User: {user} is watching {movie}")


#
# def watch_movie(user, movie):
#     rented_movie = _get_rented_movie(user, movie)
#     if not rented_movie:
#         raise MovieNotFound()
#
#     if rented_movie.views_left < 1:
#         raise ViewsLimitReached()
#
#     rented_movie.views_left -= 1
#     _start_streaming(user, movie)
#
#
# def _get_rented_movie(user, movie):
#     for rented_movie in user.rented_movies:
#         if rented_movie.movie == movie:
#             return rented_movie


def refresh_credits(acting_user, user_to_be_refreshed):
    if permissions.is_admin(acting_user) or permissions.is_moderator(acting_user):
        user_to_be_refreshed.credits_left = 5
    else:
        raise ActionNotAllowed()


def add_movie():
    new_movie = Movie(name=input("Tytul: "),
                      category=input("Kategoria: "),
                      release_date=date.fromisoformat(input("Data wydania w formacie (RRRR-MM-DD, np. 2005-05-23): ")))
    movies_directory.add_movie(new_movie)
