#!/usr/bin/env python3
"""Find all word-pair palingrams in a dictionary file.

Author: Albert Julian Tannady <me@albertjtan.com>
"""

from load_dictionary import load

words = set(load("words.txt"))


def find_palingrams():
    """Find palingrams from words."""
    palingrams = []
    for word in words:
        length = len(word)
        rev_word = word[::-1]
        if length > 1:
            for i in range(length):
                if (
                    word[i:] == rev_word[: length - i]
                    and rev_word[length - i :] in words
                ):
                    palingrams.append((word, rev_word[length - i :]))
                if (
                    word[:i] == rev_word[length - i :]
                    and rev_word[: length - i] in words
                ):
                    palingrams.append((rev_word[: length - i], word))
    return palingrams


def main():
    """Run main program."""
    palingrams = sorted(find_palingrams())
    print(f"\nNumber of palingrams = {len(palingrams)}\n")
    for first, second in palingrams:
        print(f"{first} {second}")


if __name__ == "__main__":
    main()
