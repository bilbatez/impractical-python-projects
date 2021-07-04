#!/usr/bin/env python3
"""
Anagram finder program.

Author: Albert Julian Tannady <me@albertjtan.com>
"""

import sys
from load_dictionary import load

DICT = load("words.txt")


def main():
    """Run main program."""
    print("Anagram Finder")
    print("--------------")
    print("Created by Albert JT", end="\n\n")

    while True:
        u_in = input("Input word! [input blank to quit]: ").lower()
        if not u_in:
            sys.exit("Bye-bye!")

        print()
        print("Result:")
        anagrams = find_anagrams(u_in)
        if anagrams:
            print(*anagrams, sep="\n")
        else:
            print("No result found")
        print()


def find_anagrams(word):
    """Find anagrams from input."""
    anagrams = []
    chars = sorted(list(word))
    for d_word in DICT:
        if chars == sorted(list(d_word)):
            anagrams.append(d_word)
    return anagrams


if __name__ == "__main__":
    main()
