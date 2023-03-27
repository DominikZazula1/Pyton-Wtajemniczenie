import random
from datetime import time
from enum import Enum, auto

from . import movies_directory


class Weekday(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()


weekly_schedule = {
        Weekday.MONDAY: movies_directory.available_movies[0:2],
        Weekday.TUESDAY: movies_directory.available_movies[2:4],
        Weekday.WEDNESDAY: movies_directory.available_movies[4:6],
        Weekday.THURSDAY: movies_directory.available_movies[6:8],
        Weekday.FRIDAY: movies_directory.available_movies[8:11],
        Weekday.SATURDAY: movies_directory.available_movies[11:12],
        Weekday.SUNDAY: movies_directory.available_movies[12:14],
    }


def get_schedule(weekday: Weekday):
    return weekly_schedule[weekday]


def generate_time():
    random_hour = random.randint(10, 23)
    random_minute = random.randint(0, 59)
    return time(random_hour, random_minute)
