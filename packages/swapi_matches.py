import requests
import time
from fuzzywuzzy import fuzz

def get_swapi_matches(name_one, name_two, url):
    
    character_films = []
    threshold = 0
    
    while True:
        
        # If both names were found, the loop will be aborted.
        if threshold == 2:
            print("""Both names were found. Finishing search.
            """)
            break
        
        # Requesting information to database
        print("Inspecting " + str(url[7:]))
        r = requests.get(url)
        time.sleep(0.75)
        
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
            print("""All pages were inspected.
                    """)
            break
        else:
            # Updating with the next page URL...
            url = r.json()["next"]
        
    return character_films