from datetime import datetime, date

from mod_2.new_movies import cinema_schedule
from mod_2.new_movies.cinema_schedule import Weekday


def cinema_movies_schedule(user):
    datetime_iso_format = input("When would you like to visit the cinema? (YYYY-MM-DD HH:MM): ")
    cinema_datetime = datetime.fromisoformat(datetime_iso_format)
    cinema_date = cinema_datetime.date()
    cinema_time = cinema_datetime.time()
    weekday_number = cinema_datetime.weekday()+1
    weekday = Weekday(weekday_number)
    print("This day you can watch:")
    schedule = cinema_schedule.get_movies_showtime_by_weekday(weekday)

    for movie_showtime in schedule:
        if date.today() <= cinema_date and cinema_time <= movie_showtime.showtime:
            print(f"{movie_showtime.info_with_showtime_format(user.datetime_preferences.value)} ",
                  f"{movie_showtime.movie.info_with_date_format(user.datetime_preferences.value)}")
