#!/usr/bin/python3
def roman_to_int(roman_string):
    """Convert a roman numeral to an integer."""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_string = roman_string.upper()
    numerals = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
            }
    integer = 0
    for enum, x in enumerate(roman_string):
        if enum < len(roman_string) - 1:
            if numerals[roman_string[enum + 1]] > numerals[x]:
                integer -= numerals[x]
            else:
                integer += numerals[x]
        else:
            integer += numerals[x]
    return integer
