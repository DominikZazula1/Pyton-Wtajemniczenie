
from datetime import date
from datetime import datetime
from . import permissions, movies_directory, cinema_schedule, users_directory
from .cinema_schedule import Weekday
from .configuration import UNLIMITED_WATCHING_START_DATE, UNLIMITED_WATCHING_END_DATE
from .datetime_preferences import DatetimePreference
from .movie import Movie
from .rented_movie import RentedMovie
from .exceptions import (
    NoCreditsForMovieRent,
    ActionNotAllowed,
    MovieNotFound,
    ViewsLimitReached, UserNotFound,
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
    print(f"User: {user} is watching {movie.info_with_date_format(user.datetime_preferences.value)}")


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


def cinema_movies_schedule(user):
    datetime_iso_format = input("When would you like to visit the cinema? (YYYY-MM-DD HH:MM): ")
    cinema_datetime = datetime.fromisoformat(datetime_iso_format)
    cinema_date = cinema_datetime.date()
    cinema_time = cinema_datetime.time()
    weekday_number = cinema_datetime.weekday()+1
    weekday = Weekday(weekday_number)
    print("This day you can watch:")
    schedule = cinema_schedule.get_movies_showtime_by_weekday(weekday)

    for movie_showtime in schedule:
        if date.today() <= cinema_date and cinema_time <= movie_showtime.showtime:
            print(f"{movie_showtime.info_with_showtime_format(user.datetime_preferences.value)} ",
                  f"{movie_showtime.movie.info_with_date_format(user.datetime_preferences.value)}")


def select_datetime_preferences(user):
    print("Dostępne formaty daty i czasu:")
    for option_index, datetime_preference in enumerate(DatetimePreference):
        print(f"{option_index}) {datetime_preference}")

    selected_option = int(input("Wybierz opcje: "))
    user.datetime_preferences = DatetimePreference.instance_by_index(selected_option)


def login():
    while True:
        user_login = input("Podaj login: ")
        try:
            return users_directory.find_user_by_login(user_login)
        except UserNotFound:
            print("Nie znaleziono użytkownika o podanym loginie - spróbuj ponownie")