import requests

def get_movie_from_url(url, link_set):
    r = requests.get(url)
    json = r.json()["results"]
    for movie in json:
        for index, movie_url in enumerate(link_set):
            if movie["url"] == movie_url:
                link_set[index] = movie["title"]
    return link_set