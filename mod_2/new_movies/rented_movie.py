from dataclasses import dataclass

from .movie import Movie


@dataclass
class RentedMovie:
    movie: Movie
    views_left: int = 3
