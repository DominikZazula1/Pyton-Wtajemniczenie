from new_movies.actions import cinema_movies_schedule
from new_movies.cinema_schedule import (
    generate_february_week_schedule,
    weekly_schedule,
    Weekday,
    sort_weekly_schedule,
)


def run_example():
    cinema_movies_schedule()


if __name__ == "__main__":
    run_example()
