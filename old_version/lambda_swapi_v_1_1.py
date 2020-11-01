#!/usr/bin/env python
# coding: utf-8

# # lambda_swapi
# 
# Written by **Daniel Palacio**.
# 
# ***

# In[ ]:


# Required libraries

import requests


# ***
# 
# ### SECTION 1: INPUT CLEANING
# 
# Since the API requires exact matches to retrieve the information, the inputs must be completely similar to the names stored on the API database.
# 
# The dictionary inside the following function might seem daunting, but you aren't expected to read it. Basically, it will compare your inputs to its keys, and if it detects a match, then it will clean the inputs, replacing them with the corrected values. This way, it prevents potential problems with typing mistakes or characters that can be referenced in different ways (i.e.: "Palpatine").
# 
# It also has other advantages. For instance, if you decided to ignore the input requirement of a name and a surname, then in some cases the program still will be able to match everything (i.e.: if you write "luke" and "leia", you'll still get the movies where they appear).

# In[ ]:


def input_cleaner(char1, char2):
    
    """
    It takes both character inputs and compares them to the keys from the dictionary names_dict.
    If it finds a match then it will replace the inputs' format with the values associated with that key.
    
    """
    
    names_dict = {"ADMIRAL ACKBAR":"ACKBAR",
              "BAIL ORGANA":"BAIL PRESTOR ORGANA","BERU WHITESUN":"BERU WHITESUN LARS","BERU LARS":"BERU WHITESUN LARS",
              "BIGS DARKLIGHTER":"BIGGS DARKLIGHTER",
              "C3PO":"C-3PO","CHEWBACA":"CHEWBACCA","CHEWIE":"CHEWBACCA","CLIEG LARS":"CLIEGG LARS","CORDE":"CORDÉ",
              "COUNT DOOKU":"DOOKU",
              "DARTH SIDIOUS":"PALPATINE","DEXTER JETSTER":"DEXTER JETTSTER","DORME":"DORMÉ",
              "EMPEROR PALPATINE":"PALPATINE",
              "GENERAL GRIEVOUS":"GRIEVOUS","GREDO":"GREEDO",
              "HAN":"HAN SOLO",
              "IG88":"IG-88",
              "JABBA":"JABBA DESILIJIC TIURE", "JABBA THE HUTT":"JABBA DESILIJIC TIURE",
              "KI ADI MUNDI":"KI-ADI-MUNDI","KIADIMUNDI":"KI-ADI-MUNDI","KI ADIMUNDI":"KI-ADI-MUNDI",
              "LANDO":"LANDO CALRISSIAN", "LANDO CALRISIAN":"LANDO CALRISSIAN","LEIA":"LEIA ORGANA","LUKE":"LUKE SKYWALKER",
              "MASTER YODA":"YODA",
              "OBIWAN KENOBI":"OBI-WAN KENOBI","OBI WAN KENOBI":"OBI-WAN KENOBI",
              "PADME":"PADMÉ AMIDALA","PADME AMIDALA":"PADMÉ AMIDALA","PHASMA":"CAPTAIN PHASMA",
              "PRINCESS LEIA":"LEIA ORGANA","PRINCESS LEIA ORGANA":"LEIA ORGANA",
              "QUI GON JINN":"QUI-GON JINN","QUIGON JINN":"QUI-GON JINN","QUI-GON-JINN":"QUI-GON JINN",
              "R2D2":"R2-D2","R4P17":"R4-P17","R5D4":"R5-D4","RATTS TYRELL":"RATTS TYERELL","REY SKYWALKER":"REY",
              "RIC OLIE":"RIC OLIÉ",
              "SAESSE TIIN":"SAESEE TIIN","SHAK TI":"SHAAK TI",
              "TARFUL":"TARFFUL",
              "WEDGE ANTILES":"WEDGE ANTILLES","WICKET WYSTRI WARRICK":"WICKET SYSTRI WARRICK",
              "WILLHUFF TARKIN":"WILHUFF TARKIN"
             }
    
    assert type(char1) == str and type(char2) == str, "Only strings are accepted."
            
    for key in names_dict.keys():
        
        char1 = char1.upper()
        char2 = char2.upper() # The .upper() method capitalizes the inputs.
        
        if key == char1:
            char1 = names_dict.get(key) # The .get() method retrieves the values from the selected key.
        
        if key == char2:
            char2 = names_dict.get(key)
        
        assert char1 != char2, "You repeated the same character. Restart and try again."
    
    return char1, char2


# ***
# 
# ### SECTION 2: DATA RETRIEVING 
# 
# The SWAPI database has its characters distributed across different pages. So, as a first step, we need to get the URLs of those pages, so that we can iterate the characters' names on the following step.
# 

# In[ ]:


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
   


# Having retrieved the pages URLs, we will now create a loop on them. We are going to look for the characters' names on every page, and if one of them matches the inputs we introduced, then we will append the films they appear to the *films* list.

# In[ ]:


def get_char_films(char1, char2, url_list):
    
    """
    Takes a list of URLs from SWAPI and compare the characters' names with the ones from char1 and char2.
    If there are matches, the URL of the movies where they appear will be appended to a list.
    
    """
    
    assert type(char1) == str and type(char2) == str, "Only strings are accepted."
    assert type(url_list) == list, "This argument requires a list."
    
    films_list = []
    threshold = 0
    
    for url in url_list:
        
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


# ***
# 
# ### SECTION 3: GETTING THE RESULTS
# 
# On the previous step, if there were matches, then two lists of films were appended to the *films* list. 
# 
# If that is actually the case, as we would expect, then we need to clean the values. This is because when we appended them, we didn't actually retrieve the movies' names, but a group of URLs from SWAPI that lead to information about those movies. 
# 
# This is, obviously, undesirable, so as a next step, the program will compare the URLs with the keys from the *movie_reference* dictionary, and if it finds a match, then it will return the dictionary values associated with those keys. They will be appended to the new *cleaned_films* list accordingly.
# 
# Finally, *cleaned_films* will have its duplicate values deleted, the remaining ones will be sorted and then we'll be able to visualize the results. And that is the end.
# 
# ***
# 
# **IMPORTANT NOTE**: The reason why the program needs that both inputs are matched is because it was specifically requested to be this way. 
#     
# Therefore, if one or both inputs aren't matched, the resulting output will indicate this requirement.

# In[ ]:


def get_clean_films(input_list):
    
    """
    Takes a list of movies' URLs from SWAPI and returns the actual movie names from 
    the dictionary 'movie_reference'.    
    
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


# ### FINAL SECTION: PROGRAM EXECUTION
# 
# The following cells require you to write the desired characters.
# 
# Some considerations:
# 
# - It is strongly recommended to enter the character's name and surname, in that order. As expressed before, the API requires exact matches to retrieve the information. So, for instance, if you only enter "Skywalker", then the program won't know where to look, because there are several characters with that surname.
# 
# - Obviously, single named characters ("Chewbacca", "Yoda", "Sebulba") don't have this requirement.
# 
# - Also, the program allows for certain characters to be called using their ranks or titles (i.e.: "Princess Leia", "Admiral Ackbar", "Emperor Palpatine", "General Grievous", "Count Dooku", "Darth Sidious").

# In[ ]:


input_name = input("""Enter your first character's name and surname, in that order:
    """)

input_name2 = input("""Enter your second character's name and surname, in that order:
    """)

assert input_name != input_name2, "You repeated the same character. Restart and try again."

# Executing function 1: input_cleaner
input_name, input_name2 = input_cleaner(input_name, input_name2)

print("These are your cleaned inputs:")
print("\n")
print(input_name)
print(input_name2)
print("\n")

# Executing function 2: get_url_pages
pages_list = get_url_pages()        

# Executing function 3: get_char_films
films = get_char_films(input_name, input_name2, pages_list)


# In[ ]:


# Executing function 4: get_clean_films
final_result = get_clean_films(films)

# Final results:
print("*" * 111)
print("*" * 111)
print("*" * 111)
print("\n")
print("The characters you requested were: {} and {}".format(input_name, input_name2))
print("\n")
print("\n")
print("RESULT: ", final_result)
print("\n")
print("\n")
print("Check the list above to consult for other available characters.")
print("\n")
print("*" * 111)
print("*" * 111)
print("*" * 111)

