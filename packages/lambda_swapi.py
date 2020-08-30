from packages.swapi_matches import get_swapi_matches
from packages.common_movies import get_common_movies
from packages.movie_names import get_movie_from_url

def lambda_swapi_func(first_char, second_char, people_url, movie_url):

    link_list = get_swapi_matches(first_char, second_char, people_url)

    set_results = get_common_movies(link_list)

    if type(set_results) == list:
        cleaned_results = get_movie_from_url(movie_url, set_results)
        print(" --------")
        print("| RESULT | -> The selected characters share these movies:")
        print(" --------    ", cleaned_results)
