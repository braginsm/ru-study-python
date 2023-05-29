from typing import Union
from functools import reduce


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        def map_function(movie: dict) -> float:
            return (
                float(movie["rating_kinopoisk"])
                if movie["rating_kinopoisk"] and "," in movie["country"]
                else 0
            )

        ratings = map(map_function, list_of_movies)
        rating_sum = 0.0
        movie_count = 0
        for rating in ratings:
            if rating:
                movie_count += 1
                rating_sum += rating

        return rating_sum / movie_count if movie_count > 0 else movie_count

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        def map_function(movie: dict) -> int:
            return (
                movie["name"].count("и")
                if movie["rating_kinopoisk"] and float(movie["rating_kinopoisk"]) >= rating
                else 0
            )

        counts = map(map_function, list_of_movies)

        return reduce(lambda result, count: result + count, counts)
