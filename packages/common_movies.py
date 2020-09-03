from typing import Union, List

def get_common_movies(your_list: List) -> Union[str, List]:

    """
    Checks if two characters were detected on the SWAPI database;
    if the result is positive, then it returns the common movies
    where both characters appeared.
    """

    if len(your_list) in [0, 1]:
        result_nochar = "| RESULT | -> One or both characters weren't found on the database."
        return result_nochar

    elif len(your_list) > 2:
        raise SystemExit("ERROR: There are more than two sublists on list.")

    else:
        films_char_1 = your_list[0]
        films_char_2 = your_list[1]
        set_results = sorted(list(set(films_char_1) & set(films_char_2)))

        if len(set_results) == 0:
            result_nomatch = "| RESULT | -> No matches were found."
            return result_nomatch
        else:
            return set_results
