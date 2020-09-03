import pytest
from packages.common_movies import get_common_movies

class TestGetCommonMovies(object):

	# Good arguments

	def test_no_matches(self):
		assert get_common_movies([
								["http://swapi.dev/api/films/1/"],
								["http://swapi.dev/api/films/2/"]
								]) == "| RESULT | -> No matches were found."

	def test_match(self):
		assert get_common_movies([
								[
								"http://swapi.dev/api/films/1/", 
								"http://swapi.dev/api/films/2/",
								],
								[
								"http://swapi.dev/api/films/2/",
								"http://swapi.dev/api/films/3/",
								],
								]) == ["http://swapi.dev/api/films/2/"]

	# Special arguments

	def test_empty_list(self):
		assert get_common_movies([]) == "| RESULT | -> One or both characters weren't found on the database."

	def test_single_sublist(self):
		assert get_common_movies([
                                 	[
                                    "http://swapi.dev/api/films/1/",
                                    "http://swapi.dev/api/films/2/",
                                    "http://swapi.dev/api/films/3/",
                                    "http://swapi.dev/api/films/6/"
                                    ]
                                ]) == "| RESULT | -> One or both characters weren't found on the database."

	# Bad arguments

	def test_twosublists(self):
		with pytest.raises(SystemExit):
			assert get_common_movies([
										["http://swapi.dev/api/films/1/"], 
										["http://swapi.dev/api/films/2/"], 
										["http://swapi.dev/api/films/3/"]
									])
