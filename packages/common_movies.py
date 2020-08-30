def get_common_movies(your_list):
    if len(your_list) in [0, 1]:
        print(" --------")
        print("| RESULT | -> One or both characters weren't found on the database.")
        print(" --------")
    else:
        films_char_1 = your_list[0]
        films_char_2 = your_list[1]
        set_results = list(set(films_char_1) & set(films_char_2))

        if len(set_results) == 0:
            print(" --------")
            print("| RESULT | -> No matches were found.")
            print(" --------")
        else:
            return set_results