def print_top_movies(movies, *, move_limit=10):
    movies_in_rate_order = sorted(movies, key=lambda single_movie: single_movie.rate, reverse=True)
    movies_in_rate_order = movies_in_rate_order[:move_limit]
    for index, movie in enumerate(movies_in_rate_order):
        print(f"{index + 1}. {movie}")
