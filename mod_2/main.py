
from mod_2.new_movies.actions.cinema import cinema_movies_schedule
from new_movies.actions import user as user_actions


def run_example():
    user = user_actions.login()
    user_actions.select_timezone_preferences(user)
    cinema_movies_schedule(user)


if __name__ == "__main__":
    run_example()
