from datetime import datetime, date, timedelta

from mod_2.new_movies import cinema_schedule
from mod_2.new_movies.cinema_schedule import Weekday


def cinema_movies_schedule(user):
    date_and_time_format = user.datetime_preferences.value
    datetime_iso_format = input(
        f"When would you like to visit the cinema? ({date_and_time_format.date_format}): "
    )
    cinema_date = datetime.strptime(datetime_iso_format, date_and_time_format.date_format).date()
    weekday_schedule = cinema_schedule.schedule_for_week(cinema_date, cinema_schedule.sorted_schedule)
    print("During this week you can watch:")
    for weekday, schedule_for_day in weekday_schedule.items():
        print(f"On {weekday.name}:")
        schedule = cinema_schedule.get_movies_showtime_by_weekday(weekday)
        for movie_showtime_info in schedule_for_day:
            _print_movie_showtime_info_formatted(movie_showtime_info, date_and_time_format)


def _print_movie_showtime_info_formatted(movie_showtime_info, date_and_time_format):
    showtime_formatted = movie_showtime_info.showdatetime.strftime(date_and_time_format.datetime_format)
    movie_info_formatted = movie_showtime_info.movie.info_with_date_format(date_and_time_format)
    print(f"{showtime_formatted}  {movie_info_formatted}")
