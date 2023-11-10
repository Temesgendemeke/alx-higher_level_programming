#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_numeral_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
       }
    result = 0

    for i in range(len(roman_string)):
        curr = roman_string[i]
        curr_v = roman_numeral_map[curr]
        if curr not in roman_numeral_map:
            raise ValueError(f"Invalid Roman numeral character: {curr}")
        if i + 1 < len(roman_string) and roman_numeral_map[roman_string[i + 1]] > curr_v:
            result -= curr_v
        else:
            result += curr_v
    return result
