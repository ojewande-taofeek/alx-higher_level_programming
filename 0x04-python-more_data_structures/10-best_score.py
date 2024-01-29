#!/usr/bin/python3
def best_score(a_dictionary):
    # function that returns a key with the biggest integer value
    if (a_dictionary):
        biggest = 0
        for value in a_dictionary.values():
            if value > biggest:
                biggest = value
        for key in a_dictionary.keys():
            if a_dictionary[key] == biggest:
                return key
    return
