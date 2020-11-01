import requests
import pytest

pages_list = ['https://swapi.co/api/people/', 'https://swapi.co/api/people/?page=2', 'https://swapi.co/api/people/?page=3', 'https://swapi.co/api/people/?page=4', 'https://swapi.co/api/people/?page=5', 'https://swapi.co/api/people/?page=6', 'https://swapi.co/api/people/?page=7', 'https://swapi.co/api/people/?page=8', 'https://swapi.co/api/people/?page=9']

def get_char_films(char1, char2):
    
    """
    Takes a list of URLs from SWAPI and compare the characters' names with the ones from char1 and char2.
    If there are matches, the URL of the movies where they appear will be appended to a list.
    
    """
    
    assert type(char1) == str and type(char2) == str, "Only strings are accepted."
        
    films_list = []
    threshold = 0
    
    for url in pages_list:
        
        if threshold == 2:
            print("\n")
            print("- - - All films were successfully retrieved. - - -")
            print("\n")
            break # It would be pointless to continue the loop if both characters were matched.
        
        if url == 'https://swapi.co/api/people/':
            print("\n")
            print("Getting information from page 1 ...")
        
        
        if url != 'https://swapi.co/api/people/':
            
            print("\n")
            print("Getting information from page", url[-1], "...")
                    
        r = requests.get(url)
        
        assert r.status_code == 200, "There was a problem connecting with SWAPI."
        
        data_people = r.json()["results"]
        
        for char in data_people:
            
            if threshold == 2:
                break # It would be pointless to continue the loop if both characters were matched.
            
            char_name = char["name"].upper() # This gets the character's names, in capitalized letters.
            print(char_name)
            
            if char_name == char1 or char_name == char2:
                
                print("\n")
                print("- - - There was a match! Adding films to list... - - -")
                print("\n")
                
                char_films = char["films"] # This gets the films they appear.
                # print(char_films)
                films_list.append(char_films)
                
                threshold += 1
    
    return films_list

# FUNCTION TESTING

@pytest.mark.parametrize("char1, char2, expected", [
                                                    ("LUKE SKYWALKER", "LEIA ORGANA", [
                                                    ['https://swapi.co/api/films/2/', 'https://swapi.co/api/films/6/',
                                                     'https://swapi.co/api/films/3/', 'https://swapi.co/api/films/1/', 
                                                     'https://swapi.co/api/films/7/'], 
                                                    ['https://swapi.co/api/films/2/', 'https://swapi.co/api/films/6/',
                                                     'https://swapi.co/api/films/3/', 'https://swapi.co/api/films/1/', 
                                                     'https://swapi.co/api/films/7/']
                                                    ]),
                                                    
                                                    ("PALPATINE", "GRIEVOUS", [
                                                    ['https://swapi.co/api/films/2/', 'https://swapi.co/api/films/5/',
                                                     'https://swapi.co/api/films/4/', 'https://swapi.co/api/films/6/', 
                                                     'https://swapi.co/api/films/3/'],
                                                    ['https://swapi.co/api/films/6/']
                                                    ]),
                                                    
                                                    ("C-3PO", "BB8", [
                                                    ['https://swapi.co/api/films/2/', 'https://swapi.co/api/films/5/',
                                                     'https://swapi.co/api/films/4/', 'https://swapi.co/api/films/6/', 
                                                     'https://swapi.co/api/films/3/', 'https://swapi.co/api/films/1/'], 
                                                    ['https://swapi.co/api/films/7/']
                                                    ]),
                                                    
                                                    ("OBI-WAN KENOBI", "QUI-GON JINN", [
                                                    ['https://swapi.co/api/films/2/', 'https://swapi.co/api/films/5/', 
                                                     'https://swapi.co/api/films/4/', 'https://swapi.co/api/films/6/', 
                                                     'https://swapi.co/api/films/3/', 'https://swapi.co/api/films/1/'], 
                                                    ['https://swapi.co/api/films/4/']
                                                    ]),
                                                    
                                                    ("OBI-WAN-KENOBI", "QUI-GON JINN", [
                                                    ['https://swapi.co/api/films/4/']
                                                    ]),
                                                    
                                                    ("IRON MAN", "CAPTAIN AMERICA", [])
                                                    ])
def test_get_char_films(char1, char2, expected):

    assert type(char1) == str and type(char2) == str, "Only strings are accepted."
    
    assert get_char_films(char1, char2) == expected
