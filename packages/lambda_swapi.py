from packages.swapi_matches import get_swapi_matches
from packages.common_movies import get_common_movies
from packages.movie_names import get_movie_from_url

from typing import Union, List

def lambda_swapi_func(first_char: str, second_char: str) -> Union[str, List]:

	"""
	Takes the inputted characters and returns a message indicating whether
	they were found on SWAPI, if there are movies where both characters 
	appear, and the movies titles if there were matches.
	"""

	link_list = get_swapi_matches(first_char, second_char)

	set_results = get_common_movies(link_list)

	if type(set_results) != list:
		return set_results
	else:
		cleaned_results = get_movie_from_url(set_results)
		print("\n|RESULT| -> The selected characters share these movies:")
		return cleaned_results
