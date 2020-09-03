import requests
import time
from fuzzywuzzy import fuzz
from typing import List, Optional

def get_swapi_matches(name_one: str, name_two: str) -> List[Optional[List]]:

    """
    Looks for the inputted characters on the SWAPI database and returns the 
    raw URL for every movie they appear.
    """

    if (len(name_one) == 0) \
    or (len(name_two) == 0):
        raise SystemExit("|ERROR| -> Please write some characters to search.")

    url = "http://swapi.dev/api/people/?page=1"
    character_films = []
    threshold = 0
    
    while True:
        
        # If both names were found, the loop will be aborted.
        if threshold == 2:
            character_films.sort(key=len) # If nested lists are not sorted, Unit Tests will fail.
            print("Both names were found. Finishing search.")
            return character_films
        
        # Requesting information to database
        print("Inspecting", url)
        r = requests.get(url)
        time.sleep(0.5)
        
        # Analyzing the results for matches
        json_results = r.json()["results"]
        
        for element in json_results:
            
            # If both names were found, the loop will be aborted.
            if threshold == 2:
                break
            
            if (fuzz.WRatio(element["name"], name_one) >= 75) \
            or (fuzz.WRatio(element["name"], name_two) >= 75):
                print("- " + element["name"] + " <--- MATCH DETECTED!")
                character_films.append(element["films"])
                threshold += 1
                    
        # If there are no more pages to check, this ends the loop
        if r.json()["next"] is None:
            break
        else:
            # Updating with the next page URL...
            url = r.json()["next"]

    return character_films
