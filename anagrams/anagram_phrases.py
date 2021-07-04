#!/usr/bin/env python3
"""
Check anagram phrases

Author: Albert Julian Tannady <me@albertjtan.com>
"""

import sys
from collections import Counter
from load_dictionary import load

dict_file = load("words.txt")
dict_file.append("a")
dict_file.append("i")
dict_file = sorted(dict_file)

print(r"""
 _______                                                                                     
|    |  .---.-.--------.-----.                                                               
|       |  _  |        |  -__|                                                               
|__|____|___._|__|__|__|_____|                                                               
                                                                                             
 _______                                            ______ __                                
|   _   .-----.---.-.-----.----.---.-.--------.    |   __ |  |--.----.---.-.-----.-----.----.
|       |     |  _  |  _  |   _|  _  |        |    |    __|     |   _|  _  |__ --|  -__|   _|
|___|___|__|__|___._|___  |__| |___._|__|__|__|    |___|  |__|__|__| |___._|_____|_____|__|  
                    |_____|                                                                  
""")
print("Created by: Albert Julian Tannady", end="\n\n")


def main():
    """Help user build anagram phrase from their name."""
    u_in = input("Enter a name: ")
    name = "".join(u_in.lower().split())
    name = name.replace("-", "")
    limit = len(name)
    phrase = ""
    while True:
        temp_phrase = phrase.replace(" ", "")
        if len(temp_phrase) < limit:
            print(f"Length of anagram phrase = {len(temp_phrase)}")

            find_anagrams(name, dict_file)
            print("Current anagram phrase = ")
            print(phrase, file=sys.stderr)

            choice, name = process_choice(name)
            phrase += choice + " "
        elif len(temp_phrase) == limit:
            print("\n*****FINISHED!!!*****\n")
            print("Anagram of name = ")
            print(phrase, file=sys.stderr)
            print()
            if input('\n\nTry again? (Press Enter else "n" to quit)\n').lower(
            ) == "n":
                sys.exit()
            else:
                main()


def find_anagrams(name, words):
    """Read name & dictionary file & display all anagrams IN name."""
    name_char_map = Counter(name)
    anagrams = []
    for word in words:
        curr = ""
        word_char_map = Counter(word)
        for char in word:
            if word_char_map[char] <= name_char_map[char]:
                curr += char
        if Counter(curr) == word_char_map:
            anagrams.append(word)
    print(*anagrams, sep="\n")
    print()
    print(f"Remaining letters = {name}")
    print(f"Number of remaining letters = {len(name)}")
    print(f"Number of remaining (real word) anagrams = {len(anagrams)}")


def process_choice(name):
    """Check user choice for validity, return choice & leftover letters."""
    while True:
        choice = input(
            "\nMake a choice else Enter to start over or # to end: ")
        if choice == "":
            main()
        elif choice == "#":
            sys.exit()
        else:
            candidate = "".join(choice.lower().split())
        leftovers = list(name)
        for letter in candidate:
            if letter in leftovers:
                leftovers.remove(letter)
        if len(name) - len(leftovers) == len(candidate):
            break
        else:
            print("Won't work! Make another choice!", file=sys.stderr)
    name = "".join(leftovers)
    return choice, name


if __name__ == "__main__":
    main()
