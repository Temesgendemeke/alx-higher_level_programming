#!/usr/bin/python3
def roman_to_int(roman_string):
  if not isinstance(roman_string, str):
    raise ValueError("roman_string must be a string.")
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
    current_numeral = roman_string[i]
    if current_numeral not in roman_numeral_map:
      raise ValueError(f"Invalid Roman numeral character: {current_numeral}")
    current_value = roman_numeral_map[current_numeral]
    if i + 1 < len(roman_string) and roman_numeral_map[roman_string[i + 1]] > current_value:
      result -= current_value
    else:
      result += current_value

  return result
