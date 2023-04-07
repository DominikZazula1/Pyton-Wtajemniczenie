from dataclasses import dataclass, field
from enum import Enum
from typing import List

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
    credits_left: int
    role: Role
    rented_movies: List[RentedMovie] = field(default_factory=lambda: [])
    datetime_preferences: DatetimePreference = DatetimePreference.EUROPE

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
