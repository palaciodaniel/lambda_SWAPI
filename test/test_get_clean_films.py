import pytest

def get_clean_films(input_list):
    
    """
    Takes a list of movies' URLs from SWAPI and returns the actual movie names from the dictionary 'movie_reference'.    
    
    """
        
    movie_reference = {"1": "Ep 4: A New Hope", 
                       "2": "Ep 5: The Empire Strikes Back", 
                       "3": "Ep 6: Return of the Jedi", 
                       "4": "Ep 1: The Phantom Menace", 
                       "5": "Ep 2: Attack of the Clones", 
                       "6": "Ep 3: Revenge of the Sith",
                       "7": "Ep 7: The Force Awakens"}
    
    assert type(input_list) == list, "Only a list with valid SWAPI URLs will be accepted."
    assert len(input_list) in [0, 1, 2], "The list must be either empty, or to have one or two nested lists."
    
    if len(input_list) == 0:
        return "There weren't matches for any of them. Two are required."
    
    elif len(input_list) == 1:
        return "There wasn't a match for one of them. Two are required."

    else:
        clean_films = []
    
        for group in input_list:
            for film in group:
                if film[-2] in movie_reference.keys(): # On [-2] lies the unique number for a specific movie URL.
                    movie_name = movie_reference.get(film[-2])
                    clean_films.append(movie_name)
        
        clean_films = list(sorted(set(clean_films)))
        return clean_films

# FUNCTION TESTING

@pytest.mark.parametrize("input_list, expected", [
                                                    ([
                                                    ['https://swapi.co/api/films/2/', 'https://swapi.co/api/films/6/',
                                                     'https://swapi.co/api/films/3/', 'https://swapi.co/api/films/1/', 
                                                     'https://swapi.co/api/films/7/'], 
                                                    ['https://swapi.co/api/films/2/', 'https://swapi.co/api/films/6/',
                                                     'https://swapi.co/api/films/3/', 'https://swapi.co/api/films/1/', 
                                                     'https://swapi.co/api/films/7/']
                                                    ], 
                                                    ['Ep 3: Revenge of the Sith', 'Ep 4: A New Hope', 
                                                     'Ep 5: The Empire Strikes Back', 'Ep 6: Return of the Jedi', 
                                                     'Ep 7: The Force Awakens']),
                                                    
                                                    ([
                                                    ['https://swapi.co/api/films/2/', 'https://swapi.co/api/films/5/',
                                                     'https://swapi.co/api/films/4/', 'https://swapi.co/api/films/6/', 
                                                     'https://swapi.co/api/films/3/'],
                                                    ['https://swapi.co/api/films/6/']
                                                    ], 
                                                    ['Ep 1: The Phantom Menace', 'Ep 2: Attack of the Clones', 
                                                     'Ep 3: Revenge of the Sith', 'Ep 5: The Empire Strikes Back', 
                                                     'Ep 6: Return of the Jedi']),
                                                    
                                                    ([
                                                    ['https://swapi.co/api/films/2/', 'https://swapi.co/api/films/5/',
                                                     'https://swapi.co/api/films/4/', 'https://swapi.co/api/films/6/', 
                                                     'https://swapi.co/api/films/3/', 'https://swapi.co/api/films/1/'], 
                                                    ['https://swapi.co/api/films/7/']
                                                    ], 
                                                    ['Ep 1: The Phantom Menace', 'Ep 2: Attack of the Clones', 
                                                     'Ep 3: Revenge of the Sith', 'Ep 4: A New Hope', 
                                                     'Ep 5: The Empire Strikes Back', 'Ep 6: Return of the Jedi', 
                                                     'Ep 7: The Force Awakens']),
                                                    
                                                    ([
                                                    ['https://swapi.co/api/films/2/', 'https://swapi.co/api/films/5/', 
                                                     'https://swapi.co/api/films/4/', 'https://swapi.co/api/films/6/', 
                                                     'https://swapi.co/api/films/3/', 'https://swapi.co/api/films/1/'], 
                                                    ['https://swapi.co/api/films/4/']
                                                    ], 
                                                    ['Ep 1: The Phantom Menace', 'Ep 2: Attack of the Clones', 
                                                     'Ep 3: Revenge of the Sith', 'Ep 4: A New Hope', 
                                                     'Ep 5: The Empire Strikes Back', 'Ep 6: Return of the Jedi']),
                                                    
                                                    ([
                                                    ['https://swapi.co/api/films/4/']
                                                    ], "There wasn't a match for one of them. Two are required."),
                                                    
                                                    ([], "There weren't matches for any of them. Two are required.")
                                                    ])
def test_get_clean_films(input_list, expected):

    assert type(input_list) == list, "Only a list with valid SWAPI URLs will be accepted."
    assert len(input_list) in [0, 1, 2], "The list must be either empty, or to have one or two nested lists."

    assert get_clean_films(input_list) == expected
