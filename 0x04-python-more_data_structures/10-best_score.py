#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_v = None
    best_c = 0
    for key, value in a_dictionary.items():
        if value > best_c:
            best_v = key
            best_c = value
    return best_v
