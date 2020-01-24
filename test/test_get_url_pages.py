import pytest
import requests

def get_url_pages():
    
    """
    Takes a URL from SWAPI and then return all the pages related to that category. They will be stored on a list.
    
    """
    url = "https://swapi.co/api/people/"
    pages_url = []
    
    while True:
        
        pages_url.append(url)
        
        r = requests.get(url)
        
        assert r.status_code == 200, "There was a problem connecting with SWAPI."
        
        url = r.json()["next"] # If there are more pages to check, this will update the URL accordingly.
        
        if url is None: # If there are no more pages to check, this finishes the function.
            
            print("\n")
            print("- - - All URLs were successfully retrieved. - - -")
            
            return pages_url
            break
            
        print("Getting URL from page", url[-1], "...")

# FUNCTION TESTING

@pytest.fixture
def input_value():
    input = ['https://swapi.co/api/people/', 'https://swapi.co/api/people/?page=2', 'https://swapi.co/api/people/?page=3', 'https://swapi.co/api/people/?page=4', 'https://swapi.co/api/people/?page=5', 'https://swapi.co/api/people/?page=6', 'https://swapi.co/api/people/?page=7', 'https://swapi.co/api/people/?page=8', 'https://swapi.co/api/people/?page=9']
    return input

def test_get_url_pages(input_value):
    assert get_url_pages() == input_value


