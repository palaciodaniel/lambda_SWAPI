import pytest
from packages.swapi_matches import get_swapi_matches

class TestGetSwapiMatches(object):
    
    # Good arguments
    
    def test_correct_inputs_exactmatch(self):
        assert get_swapi_matches("yoda", "palpatine") == sorted([
                                                                    [
                                                                    "http://swapi.dev/api/films/2/", 
                                                                    "http://swapi.dev/api/films/3/", 
                                                                    "http://swapi.dev/api/films/4/", 
                                                                    "http://swapi.dev/api/films/5/", 
                                                                    "http://swapi.dev/api/films/6/"
                                                                    ], 
                                                                    [
                                                                    "http://swapi.dev/api/films/2/", 
                                                                    "http://swapi.dev/api/films/3/", 
                                                                    "http://swapi.dev/api/films/4/", 
                                                                    "http://swapi.dev/api/films/5/", 
                                                                    "http://swapi.dev/api/films/6/"]
                                                                ], key=len)
        
        assert get_swapi_matches("mace windu", "darth maul") == sorted([
                                                                            [
                                                                            "http://swapi.dev/api/films/4/", 
                                                                            "http://swapi.dev/api/films/5/", 
                                                                            "http://swapi.dev/api/films/6/"
                                                                            ], 
                                                                            [
                                                                            "http://swapi.dev/api/films/4/"
                                                                            ]
                                                                        ], key=len)
        
        assert get_swapi_matches("han solo", "chewbacca") == sorted([
                                                                        [
                                                                        "http://swapi.dev/api/films/1/", 
                                                                        "http://swapi.dev/api/films/2/", 
                                                                        "http://swapi.dev/api/films/3/"
                                                                        ], 
                                                                        [
                                                                        "http://swapi.dev/api/films/1/", 
                                                                        "http://swapi.dev/api/films/2/", 
                                                                        "http://swapi.dev/api/films/3/", 
                                                                        "http://swapi.dev/api/films/6/"
                                                                        ]
                                                                    ], key=len)
        
        # Despite being the same character, there are still two entries for him. Probably
        # due to the "becoming another person" reference from Episode VI.
        
        assert get_swapi_matches("anakin skywalker", "darth vader") == sorted([
                                                                                  [
                                                                                  "http://swapi.dev/api/films/4/", 
                                                                                  "http://swapi.dev/api/films/5/", 
                                                                                  "http://swapi.dev/api/films/6/"
                                                                                  ], 
                                                                                  [
                                                                                  "http://swapi.dev/api/films/1/", 
                                                                                  "http://swapi.dev/api/films/2/", 
                                                                                  "http://swapi.dev/api/films/3/", 
                                                                                  "http://swapi.dev/api/films/6/"
                                                                                  ]
                                                                              ], key=len)   
    
    # Special arguments
    
    def test_correct_inputs_nohyphen(self):
        
        # Actual names on SWAPI: "C-3PO" and "R2-D2".
        
        assert get_swapi_matches("c3po", "r2d2") == sorted([
                                                               [
                                                               "http://swapi.dev/api/films/1/", 
                                                               "http://swapi.dev/api/films/2/", 
                                                               "http://swapi.dev/api/films/3/", 
                                                               "http://swapi.dev/api/films/4/", 
                                                               "http://swapi.dev/api/films/5/", 
                                                               "http://swapi.dev/api/films/6/"
                                                               ], 
                                                               [
                                                               "http://swapi.dev/api/films/1/",
                                                               "http://swapi.dev/api/films/2/",
                                                               "http://swapi.dev/api/films/3/",
                                                               "http://swapi.dev/api/films/4/",
                                                               "http://swapi.dev/api/films/5/",
                                                               "http://swapi.dev/api/films/6/"
                                                               ]
                                                           ], key=len)
        
        
    
    def test_correct_inputs_incomplete(self):
        
        # Actual names on SWAPI: "Luke Skywalker" and "Leia Organa".
        # These inputs are missing the surnames.
        
        assert get_swapi_matches("luke", "leia") == sorted([
                                                               [
                                                               "http://swapi.dev/api/films/1/",
                                                               "http://swapi.dev/api/films/2/",
                                                               "http://swapi.dev/api/films/3/",
                                                               "http://swapi.dev/api/films/6/"
                                                               ],
                                                               [
                                                               "http://swapi.dev/api/films/1/",
                                                               "http://swapi.dev/api/films/2/",
                                                               "http://swapi.dev/api/films/3/",
                                                               "http://swapi.dev/api/films/6/"
                                                               ]
                                                           ], key=len)
        
        # Actual names on SWAPI: "Qui-Gon Jinn" and "Obi-Wan Kenobi".
        
        assert get_swapi_matches("qui gon", "obi wan") == sorted([
                                                                      [
                                                                      "http://swapi.dev/api/films/4/"
                                                                      ],
                                                                      [
                                                                      "http://swapi.dev/api/films/1/",
                                                                      "http://swapi.dev/api/films/2/",
                                                                      "http://swapi.dev/api/films/3/",
                                                                      "http://swapi.dev/api/films/4/",
                                                                      "http://swapi.dev/api/films/5/",
                                                                      "http://swapi.dev/api/films/6/"
                                                                      ]
                                                                 ], key=len)
        
        # Actual names on SWAPI: "Padmé Amidala" and "Darth Vader".
        
        assert get_swapi_matches("padme", "vader") == sorted([   
                                                                 [
                                                                 "http://swapi.dev/api/films/4/",
                                                                 "http://swapi.dev/api/films/5/",
                                                                 "http://swapi.dev/api/films/6/"
                                                                 ], 
                                                                 [
                                                                 "http://swapi.dev/api/films/1/",
                                                                 "http://swapi.dev/api/films/2/",
                                                                 "http://swapi.dev/api/films/3/",
                                                                 "http://swapi.dev/api/films/6/"
                                                                 ]
                                                             ], key=len)
        
    
    def test_correct_inputs_typo(self):
        
        # Actual names on SWAPI: "Boba Fett" and "Lando Calrissian".
        
        assert get_swapi_matches("boba feet", "lando calrisian") == sorted([
                                                                                [
                                                                                "http://swapi.dev/api/films/2/",
                                                                                "http://swapi.dev/api/films/3/",
                                                                                "http://swapi.dev/api/films/5/"
                                                                                ]
                                                                                , 
                                                                                [
                                                                                "http://swapi.dev/api/films/2/",
                                                                                "http://swapi.dev/api/films/3/"
                                                                                ]
                                                                           ], key=len)
                                 
    def test_correct_inputs_addedword(self):
        
        # These inputs include the ranks.
        
        # Actual names on SWAPI: "Ackbar" and "Grievous".
                
        assert get_swapi_matches("general ackbar", "general grievous") == sorted([
                                                                                      [
                                                                                      "http://swapi.dev/api/films/3/"
                                                                                      ], 
                                                                                      [
                                                                                      "http://swapi.dev/api/films/6/"
                                                                                      ]
                                                                                 ], key=len)
        
        # Actual names on SWAPI: "Dooku" and "Yoda".
        
        assert get_swapi_matches("count dooku", "master yoda") == sorted([
                                                                              [
                                                                              "http://swapi.dev/api/films/5/",
                                                                              "http://swapi.dev/api/films/6/"
                                                                              ], 
                                                                              [
                                                                              "http://swapi.dev/api/films/2/",
                                                                              "http://swapi.dev/api/films/3/",
                                                                              "http://swapi.dev/api/films/4/",
                                                                              "http://swapi.dev/api/films/5/",
                                                                              "http://swapi.dev/api/films/6/"
                                                                              ]
                                                                          ], key=len)
    
    def test_correct_inputs_changedword(self):
                                 
        # Actual names on SWAPI: "Jabba Desilijic Tiure" and "Obi-Wan Kenobi".
        
        assert get_swapi_matches("jabba the hutt", "ben kenobi") == sorted([
                                                                                [
                                                                                "http://swapi.dev/api/films/1/",
                                                                                "http://swapi.dev/api/films/3/",
                                                                                "http://swapi.dev/api/films/4/"
                                                                                ], 
                                                                                [
                                                                                "http://swapi.dev/api/films/1/",
                                                                                "http://swapi.dev/api/films/2/",
                                                                                "http://swapi.dev/api/films/3/",
                                                                                "http://swapi.dev/api/films/4/",
                                                                                "http://swapi.dev/api/films/5/",
                                                                                "http://swapi.dev/api/films/6/"
                                                                            ]
                                                                            ], key=len)
        
    
    # Bad arguments
    
    def test_incomplete_arguments(self):

        with pytest.raises(TypeError):
            get_swapi_matches("leia")

    def test_empty_inputs(self):

        with pytest.raises(SystemExit):
            assert get_swapi_matches("", "")

        with pytest.raises(SystemExit):
            assert get_swapi_matches("", "leia")

    def test_nonexistent_inputs(self):

        # Some of the following inputs do not belong to Star Wars.

        assert get_swapi_matches("iron man", "captain america") == []

        assert get_swapi_matches("thor", "leia") == [
                                                        [
                                                        "http://swapi.dev/api/films/1/",
                                                        "http://swapi.dev/api/films/2/",
                                                        "http://swapi.dev/api/films/3/",
                                                        "http://swapi.dev/api/films/6/"
                                                        ]
                                                    ]