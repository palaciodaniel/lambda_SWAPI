import pytest
from packages.movie_names import get_movie_from_url

class TestGetMovieFromUrl(object):

	# Good arguments

	def test_newhope(self):
		assert get_movie_from_url(["http://swapi.dev/api/films/1/"]) == ["4. A New Hope"]

	def test_empirestrikesback(self):
		assert get_movie_from_url(["http://swapi.dev/api/films/2/"]) == ["5. The Empire Strikes Back"]

	def test_returnjedi(self):
		assert get_movie_from_url(["http://swapi.dev/api/films/3/"]) == ["6. Return of the Jedi"]

	def test_phantomenace(self):
		assert get_movie_from_url(["http://swapi.dev/api/films/4/"]) == ["1. The Phantom Menace"]

	def test_attackclones(self):
		assert get_movie_from_url(["http://swapi.dev/api/films/5/"]) == ["2. Attack of the Clones"]

	def test_revengesith(self):
		assert get_movie_from_url(["http://swapi.dev/api/films/6/"]) == ["3. Revenge of the Sith"]

	def test_sortedmovies(self):
		assert get_movie_from_url([
									"http://swapi.dev/api/films/1/", 
									"http://swapi.dev/api/films/2/",
									"http://swapi.dev/api/films/3/", 
									"http://swapi.dev/api/films/4/", 
									"http://swapi.dev/api/films/5/", 
									"http://swapi.dev/api/films/6/"
								 ]) == [
										"1. The Phantom Menace", 
										"2. Attack of the Clones", 
										"3. Revenge of the Sith", 
										"4. A New Hope", 
										"5. The Empire Strikes Back", 
										"6. Return of the Jedi"
										]

	# Bad arguments

	def test_empty_set_results(self):
		with pytest.raises(SystemExit):
			assert get_movie_from_url([])

	def test_longerthansix(self):
		with pytest.raises(SystemExit):
			assert get_movie_from_url([
										"http://swapi.dev/api/films/1/", 
										"http://swapi.dev/api/films/2/",
										"http://swapi.dev/api/films/3/", 
										"http://swapi.dev/api/films/4/", 
										"http://swapi.dev/api/films/5/", 
										"http://swapi.dev/api/films/6/",
										"http://swapi.dev/api/films/6/"
								 	  ])

	def test_incorrect_url(self):
		with pytest.raises(SystemExit):
			assert get_movie_from_url(["http://swapi.dev/api/films/7/"])

	def test_duplicate_url(self):
		with pytest.raises(SystemExit):
			assert get_movie_from_url([
										"http://swapi.dev/api/films/1/", 
										"http://swapi.dev/api/films/1/"
									  ])