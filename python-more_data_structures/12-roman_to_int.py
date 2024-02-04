#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == None:
        return 0
    roman_numbers = { 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10,
    'V': 5, 'I': 1 }
    decimal_numbers = []
    for x in roman_string:
        if x in roman_numbers:
            decimal_numbers.append(roman_numbers[x])
    n = 0
    for i in range(len(decimal_numbers) - 1):
        if decimal_numbers[i] < decimal_numbers[i + 1]:
            decimal_numbers[i] *= -1
    return sum(decimal_numbers)
