from datetime import date

from .exceptions import UserNotFound
from .user import User, Role

available_users = [
    User(
        first_name="dominik",
        last_name="z",
        login="dz",
        birth_date=date(year=1980, month=1, day=1),
        # birth_date=date(year=2015, month=1, day=1),
        credits_left=5,
        role=Role.USER,
        rented_movies=[],
    )
]


def find_user_by_login(login):
    lower_case_login = login.lower()
    for user in available_users:
        if lower_case_login == user.login.lower():
            return user
    raise UserNotFound()
