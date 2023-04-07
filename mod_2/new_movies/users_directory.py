from .exceptions import UserNotFound
from .user import User, Role

available_users = [User("Dominik", "Dominik", "Z", 100, Role.USER, )]


def find_user_by_login(login):
    lower_case_login = login.lower()
    for user in available_users:
        if lower_case_login == user.login.lower():
            return user
    raise UserNotFound()
