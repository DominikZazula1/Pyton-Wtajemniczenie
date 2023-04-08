from datetime import date

from mod_2.new_movies import movies_directory
from mod_2.new_movies.configuration import UNLIMITED_WATCHING_START_DATE, UNLIMITED_WATCHING_END_DATE
from mod_2.new_movies.exceptions import MovieNotFound, ViewsLimitReached, NoCreditsForMovieRent
from mod_2.new_movies.movie import Movie
from mod_2.new_movies.rented_movie import RentedMovie


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
    print(f"User: {user} is watching {movie.info_with_date_format(user.datetime_preferences.value)}")


def add_movie():
    new_movie = Movie(name=input("Tytul: "),
                      category=input("Kategoria: "),
                      release_date=date.fromisoformat(input("Data wydania w formacie (RRRR-MM-DD, np. 2005-05-23): ")))
    movies_directory.add_movie(new_movie)


def rent_movie(user, movie):
    if user.credits_left < 1:
        raise NoCreditsForMovieRent()
    user.rented_movies.append(RentedMovie(movie))
    user.credits_left -= 1
