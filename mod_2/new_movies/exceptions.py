class MovieAlreadySeen(ValueError):
    def __init__(self, message=None):
        if message is None:
            message = "You have already seen this movie!"
        super().__init__(message)


class InvalidRateValue(ValueError):
    def __init__(self, message=None):
        if message is None:
            message = "Movie rate must be a number greater than 0 and lower than 6"
        super().__init__(message)


class NoCreditsForMovieRent:
    pass


class ActionNotAllowed:
    pass


class MovieNotFound:
    pass


class ViewsLimitReached:
    pass


class UserNotFound(Exception):
    pass


class TooYoungForMovie(Exception):
    pass