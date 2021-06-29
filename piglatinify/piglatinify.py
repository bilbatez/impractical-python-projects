#!/usr/bin/env python3
"""
Pig Latin-ify

Author: Albert Julian Tannady <me@albertjtan.com>
"""

import re
import sys
from string import punctuation

SPLITTER = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")
VOWELS = "aeiou"


def welcome():
    """Greeting"""
    greeting = r"""
  _____                                  _   _       _  __       _             
 |_   _|                            /\  | | (_)     (_)/ _|     | |            
   | |  __ _ _ __   __ _ _   _     /  \ | |_ _ _ __  _| |_ _   _| | __ _ _   _ 
   | | / _` | '_ \ / _` | | | |   / /\ \| __| | '_ \| |  _| | | | |/ _` | | | |
  _| || (_| | |_) | (_| | |_| |  / ____ \ |_| | | | | | | | |_| | | (_| | |_| |
 |_____\__, | .__/ \__,_|\__, | /_/    \_\__|_|_| |_|_|_|  \__, |_|\__,_|\__, |
        __/ | |           __/ |                             __/ |         __/ |
       |___/|_|          |___/                             |___/         |___/ 
"""
    print(greeting)


def main():
    """Main Program"""
    welcome()
    print("reatedcay ybay: albertay tjay")
    print()
    while True:
        u_in = input("inputway hetay entencesay! [q otay uitqay]: ").lower()
        if u_in == "q":
            sys.exit("yebay-yebay!")

        if u_in:
            print("".join([convert(word) for word in SPLITTER.split(u_in)]))
        else:
            print("ustmay otnay ebay emptyyay!", file=sys.stderr)
        print()


def convert(word):
    """Pig Latin-ify"""
    if word and not __has_number_or_punctuation(word):
        if word[0] in VOWELS:
            word = word + "way"
        elif len(word) > 1:
            word = word[1:] + word[0] + "ay"
    return word


def __has_number_or_punctuation(word):
    """Check has number or punctuation"""
    return __has_number(word) or __has_punctuation(word)


def __has_number(word):
    """Check numbers"""
    return any(char.isdigit() for char in word)


def __has_punctuation(word):
    """Check punctuations"""
    return any(char in punctuation for char in word)


if __name__ == "__main__":
    main()
