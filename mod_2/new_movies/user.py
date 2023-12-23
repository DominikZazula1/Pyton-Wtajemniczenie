from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import List

from . import datetime_utils
from .datetime_preferences import DatetimePreference
from .rented_movie import RentedMovie


class Role(Enum):
    ADMIN = "ADMIN"
    MODERATOR = "MODERATOR"
    USER = "USER"


@dataclass
class User:
    login: str
    first_name: str
    last_name: str
    birth_date: date
    credits_left: int
    role: Role
    rented_movies: List[RentedMovie] = field(default_factory=lambda: [])
    datetime_preferences: DatetimePreference = DatetimePreference.EUROPE

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        return datetime_utils.full_years_between_dates(date.today(), self.birth_date)