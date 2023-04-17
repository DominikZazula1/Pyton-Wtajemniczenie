from mod_2.new_movies import permissions, users_directory
from mod_2.new_movies.datetime_preferences import DatetimePreference
from mod_2.new_movies.exceptions import ActionNotAllowed, UserNotFound


def refresh_credits(acting_user, user_to_be_refreshed):
    if permissions.is_admin(acting_user) or permissions.is_moderator(acting_user):
        user_to_be_refreshed.credits_left = 5
    else:
        raise ActionNotAllowed()


def select_datetime_preferences(user):
    print("Available formats:")
    for option_index, datetime_preference in enumerate(DatetimePreference):
        print(f"{option_index}) {datetime_preference}")

    selected_option = int(input("Select an option: "))
    user.datetime_preferences = DatetimePreference.instance_by_index(selected_option)


def login():
    while True:
        user_login = input("Login: ")
        try:
            return users_directory.find_user_by_login(user_login)
        except UserNotFound:
            print("User with given login not found - try again")
