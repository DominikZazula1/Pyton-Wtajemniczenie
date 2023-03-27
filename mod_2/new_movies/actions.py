from datetime import date

from . import permissions, movies_directory, cinema_schedule
from .cinema_schedule import Weekday
from .configuration import UNLIMITED_WATCHING_START_DATE, UNLIMITED_WATCHING_END_DATE
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


def cinema_movies_schedule():
    cinema_date_input = input("When would you like to visit the cinema? (YYYY-MM-DD): ")
    cinema_date = date.fromisoformat(cinema_date_input)
    weekday_number = cinema_date.isoweekday()
    weekday = Weekday(weekday_number)
    print("This day you can watch:")
    schedule = cinema_schedule.get_movies_showtime_by_weekday(weekday)
    sorted_schedule = sorted(schedule, key=lambda movie: movie.showtime)
    for movie_showtime in sorted_schedule:
        print(f"{movie_showtime.showtime} {movie_showtime.movie}")