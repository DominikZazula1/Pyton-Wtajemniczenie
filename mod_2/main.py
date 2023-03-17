
from new_movies import movies_ranking, actions, movies_directory


def run_example():
    print(movies_directory.available_movies[0].today_date)
    actions.add_movie()
    print(movies_directory.available_movies[-1].today_date)


if __name__ == "__main__":
    run_example()
