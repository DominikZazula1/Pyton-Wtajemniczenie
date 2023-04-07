from dataclasses import dataclass
from enum import Enum, auto

import datetime as datetime

from . import movies_directory
from .movie import Movie


class Weekday(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()


@dataclass
class MovieShowtime:
    movie: Movie
    showtime: datetime.time


@dataclass
class MovieShowDatetime:
    movie: Movie
    showdatetime: datetime

    @staticmethod
    def from_movie_showtime_and_date(movie_showtime: MovieShowtime, movie_date: datetime.date):
        date_time = datetime.datetime.combine(movie_date, movie_showtime.showtime)
        return MovieShowDatetime(movie_showtime.movie, date_time)


weekly_schedule = {
    Weekday.MONDAY: [
        MovieShowtime(movies_directory.available_movies[0], datetime.time(15, 15)),
        MovieShowtime(movies_directory.available_movies[1], datetime.time(17, 15)),
    ],
    Weekday.TUESDAY: [
        MovieShowtime(movies_directory.available_movies[3], datetime.time(17, 15)),
        MovieShowtime(movies_directory.available_movies[2], datetime.time(15, 15)),
    ],
    Weekday.WEDNESDAY: [
        MovieShowtime(movies_directory.available_movies[4], datetime.time(15, 15)),
        MovieShowtime(movies_directory.available_movies[5], datetime.time(17, 15)),
    ],
    Weekday.THURSDAY: [
        MovieShowtime(movies_directory.available_movies[7], datetime.time(17, 15)),
        MovieShowtime(movies_directory.available_movies[6], datetime.time(15, 15)),
    ],
    Weekday.FRIDAY: [
        MovieShowtime(movies_directory.available_movies[10], datetime.time(19, 20)),
        MovieShowtime(movies_directory.available_movies[8], datetime.time(15, 15)),
        MovieShowtime(movies_directory.available_movies[9], datetime.time(17, 15)),
    ],
    Weekday.SATURDAY: [MovieShowtime(movies_directory.available_movies[11], datetime.time(18, 00))],
    Weekday.SUNDAY: [
        MovieShowtime(movies_directory.available_movies[12], datetime.time(13, 25)),
        MovieShowtime(movies_directory.available_movies[13], datetime.time(14, 50)),
    ],
}


def sort_weekly_schedule(schedule):
    return {
        weekday: sorted(showtime, key=lambda movie_showtime: movie_showtime.showtime)
        for weekday, showtime in schedule.items()
    }


def get_movies_showtime_by_weekday(weekday: Weekday):
    sorted_schedule = sort_weekly_schedule(weekly_schedule)
    return sorted_schedule[weekday]


def generate_february_week_schedule(schedule):
    february_21 = datetime.date(year=2021, month=2, day=21)

    result = {}
    for weekday, showtimes in schedule.items():
        particular_weekday_in_february = february_21.replace(day=february_21.day + weekday.value)
        result[weekday] = [
            MovieShowDatetime.from_movie_showtime_and_date(
                movie_showtime, particular_weekday_in_february
            )
            for movie_showtime in showtimes
        ]
    return result
