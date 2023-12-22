from datetime import date, timedelta

UNLIMITED_WATCHING_START_DATE = date.fromisoformat("2023-03-01")
UNLIMITED_WATCHING_END_DATE = date.fromisoformat("2023-03-31")

AUTH_FAILED_LIMIT = 2
AUTH_FAILED_EXTENDED_LIMIT = 4
AUTH_FAILED_LOCK_TIME = timedelta(seconds=5)



