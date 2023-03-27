from datetime import date

from . import permissions, movies_directory
from .cinema_schedule import get_schedule, Weekday, generate_time
from .configuration import UNLIMITED_WATCHING_START_DATE, UNLIMITED_WATCHING_END_DATE
from .movie import Movie
from .rented_movie import RentedMovie
from .exceptions import (
    NoCreditsForMovieRent,
    ActionNotAllowed,
    MovieNotFound,
    ViewsLimitReached,
)


def cinema_movies_schedule():
    iso_date = input("When would you like to visit cinema? ")
    weekday = date.fromisoformat(iso_date).isoweekday()
    print("This day you can watch: ")
    schedule = get_schedule(Weekday(weekday))
    for movie in schedule:
        print(movie, f"Start at: {generate_time()}")


def rent_movie(user, movie):
    if user.credits_left < 1:
        raise NoCreditsForMovieRent()
    user.rented_movies.append(RentedMovie(movie))
    user.credits_left -= 1


def watch_movie(user, movie):
    rented_movie = _get_rented_movie(user, movie)
    if not rented_movie:
        raise MovieNotFound()

    if _unlimited_watching_promo():
        _watch_movie_during_unlimited_promo(user, rented_movie)
    else:
        _watch_movie_during_standard_period(user, rented_movie)


def _get_rented_movie(user, movie):
    for rented_movie in user.rented_movies:
        if rented_movie.movie == movie:
            return rented_movie


def _unlimited_watching_promo():
    return UNLIMITED_WATCHING_START_DATE <= date.today() <= UNLIMITED_WATCHING_END_DATE


def _watch_movie_during_unlimited_promo(user, rented_movie):
    _start_streaming(user, rented_movie.movie)


def _watch_movie_during_standard_period(user, rented_movie):
    if rented_movie.views_left < 1:
        raise ViewsLimitReached()

    rented_movie.views_left -= 1
    _start_streaming(user, rented_movie.movie)


def _start_streaming(user, movie):
    print(f"User: {user} is watching {movie}")


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
