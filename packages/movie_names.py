import requests
from typing import List

def get_movie_from_url(link_set: List) -> List:

	"""
	Takes the raw URLs of movies where both characters appeared, and
	returns the sorted movie names accordingly.
	"""

	correct_urls = ["https://swapi.dev/api/films/1/", "https://swapi.dev/api/films/2/", "https://swapi.dev/api/films/3/", "https://swapi.dev/api/films/4/", "https://swapi.dev/api/films/5/", "https://swapi.dev/api/films/6/"]

	# Checking for incorrect elements on list:

	for url in link_set:
		if url not in correct_urls:
			raise SystemExit("|ERROR| -> Wrong URL on list.")

	if (len(link_set) > 6) \
	or (len(link_set) == 0):
		raise SystemExit("|ERROR| -> Wrong list length (it should be 1-6).")

	elif (len(link_set) != len(set(link_set))):
		raise SystemExit("|ERROR| -> List should not have duplicate values.")

	# If the function reaches this section, it means everything is valid.

	url = "http://swapi.dev/api/films/"
	r = requests.get(url)
	json = r.json()["results"]

	for ep in json:
		for i, mov_url in enumerate(link_set):
			if ep["url"] == mov_url:
				link_set[i] = str(ep["episode_id"]) + ". " + ep["title"]

	return sorted(link_set)
