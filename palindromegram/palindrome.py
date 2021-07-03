#!/usr/bin/env python3
"""
Find palindromes (letter palingrams) in a dictionary file.

Author: Albert Julian Tannady <me@albertjtan.com>
"""

from load_dictionary import load

words = load("words.txt")


def find_palindromes():
    """Find palindromes."""
    palindromes = []
    for word in words:
        if len(word) > 1 and word == word[::-1]:
            palindromes.append(word)
    return palindromes


def find_palindromes_recursively():
    """Find palindromes recursively."""
    palindromes = []
    for word in words:

        def rec_palindrome(word):
            if len(word) <= 1:
                return True

            if word[0] == word[-1]:
                return rec_palindrome(word[1:-1])
            return False

        if rec_palindrome(word):
            palindromes.append(word)
    return palindromes


def main():
    """Run main program."""
    palindromes = find_palindromes()

    print(f"\nNumber of palindromes found = {len(palindromes)}\n")
    print(*palindromes, sep="\n")


if __name__ == "__main__":
    main()
