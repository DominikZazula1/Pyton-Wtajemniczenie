from datetime import datetime

from mod_2.new_movies import movies_directory
from mod_2.new_movies.configuration import UNLIMITED_WATCHING_START_DATE, UNLIMITED_WATCHING_END_DATE
from mod_2.new_movies.exceptions import MovieNotFound, ViewsLimitReached, NoCreditsForMovieRent, TooYoungForMovie
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
    return UNLIMITED_WATCHING_START_DATE <= datetime.today().date() <= UNLIMITED_WATCHING_END_DATE


def _watch_movie_during_unlimited_promo(user, rented_movie):
    _start_streaming(user, rented_movie.movie)


def _watch_movie_during_standard_period(user, rented_movie):
    if rented_movie.views_left < 1:
        raise ViewsLimitReached()

    rented_movie.views_left -= 1
    _start_streaming(user, rented_movie.movie)


def _start_streaming(user, movie):
    print(f"User: {user} is watching {movie.info_with_date_format(user.datetime_preferences.value)}")


def add_movie(user):
    print("Adding new movie")
    print("Provide movie's data")
    name = input("Title: ")
    category = input("Category: ")
    date_and_time_format = user.datetime_preferences.value
    release_date_input = input(f"Release date (in {date_and_time_format.date_format} format): ")
    release_date = datetime.strptime(release_date_input, date_and_time_format.date_format).date()
    new_movie = Movie(name=name,
                      category=category,
                      release_date=release_date)
    movies_directory.add_movie(new_movie)
    print(f"Movie added: {new_movie.info_with_date_format(date_and_time_format)}")


def rent_movie(user, movie):
    if user.credits_left < 1:
        raise NoCreditsForMovieRent()
    if not movie.is_age_appropriate_to_watch(user.age):
        raise TooYoungForMovie()
    user.rented_movies.append(RentedMovie(movie))
    user.credits_left -= 1
