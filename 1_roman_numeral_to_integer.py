#! /usr/bin/python3
# -*- coding: utf-8 -*-

__copyright__ = "Copyright (c) 2019 Puneeth Kosaraju. All Rights Reserved."
__author__ = "Puneeth Kosaraju"
__maintainer__ = "Puneeth Kosaraju"
__version__ = "1.0.0"

##########################################################################################################
# Main Method to translate ROMAN numerals into integer
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
##########################################################################################################

import re
import os
import traceback

class RomanNumeralConverter:

    allowed_characters = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    min_str_length = 1
    max_str_length = 8
    roman_numeral_re = "^[IVXLCDM]{1,8}$"

    ##########################################################################################################
    # Method to validate input string
    ##########################################################################################################
    def validate_input(self, s):
        
        if not re.search(self.roman_numeral_re, s):
            print("*** Error: {0}, Please re-try again!".format("Invalid Roman Numeral"))
            os._exit(1)

    ##########################################################################################################
    # Method to convert roman numerals into integer value
    ##########################################################################################################
    def convert(self, s):

        total = 0

        for i in range(len(s)):

            # value of current character
            current_char_val = self.allowed_characters[s[i]]
            #value of next character
            next_char_val = self.allowed_characters[s[i+1]] if (i+1 < len(s)) else 0
            # multiplication factor of current char based on precedence
            multiply_factor = -1 if current_char_val < next_char_val else 1
            # add to total
            total = total + ( current_char_val * multiply_factor)
    
        return total

if __name__ == '__main__':
    try:
        converter = RomanNumeralConverter()

        roman_numeral_str = str(input("Please enter Roman Numerals? "))
        converter.validate_input(roman_numeral_str)

        # Invoke class method to convert roman numeral into integer
        roman_numeral_value = converter.convert(roman_numeral_str)

        print("Intger Value: {0}".format(roman_numeral_value))
    except Exception as e:
        print("Unexpected error occurred. Details: ")
        traceback.print_exc()
