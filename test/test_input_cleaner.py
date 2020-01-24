import pytest

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
    assert type(names_dict) == dict, "This argument requires a dictionary."
        
    for key in names_dict.keys():
        
        char1 = char1.upper()
        char2 = char2.upper() # The .upper() method capitalizes the inputs.
        
        if key == char1:
            char1 = names_dict.get(key) # The .get() method retrieves the values from the selected key.
        
        if key == char2:
            char2 = names_dict.get(key)
    
    return char1, char2

# FUNCTION TESTING

@pytest.mark.parametrize("char1, char2, expected", [
                                                    ("luke", "leia", ("LUKE SKYWALKER", "LEIA ORGANA")),
                                                    ("darth sidious", "general grievous", ("PALPATINE", "GRIEVOUS")),
                                                    ("c3po", "bb8", ("C-3PO", "BB8")),
                                                    ("obi wan kenobi", "qui gon jinn", ("OBI-WAN KENOBI", "QUI-GON JINN")),
                                                    ("obi-wan-kenobi", "qui-gon-jinn", ("OBI-WAN-KENOBI", "QUI-GON JINN")),
                                                    ("iron man", "captain america", ("IRON MAN", "CAPTAIN AMERICA"))
                                                    ])
def test_input_cleaner(char1, char2, expected):

    assert type(char1) == str and type(char2) == str, "Only strings are accepted."
    
    assert input_cleaner(char1, char2) == expected
