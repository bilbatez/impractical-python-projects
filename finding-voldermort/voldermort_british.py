#!/usr/bin/env python3
"""
Finding Voldermort.

Author: Albert Julian Tannady <me@albertjtan.com>
"""

import sys
from itertools import permutations
from collections import Counter
from load_dictionary import load


def main():
    """Load files, run filters, allow user to view anagrams by 1st letters."""
    name = "tmvoordle".lower()

    filtered = cv_map_filter(name)
    filtered = trigram_filter(filtered)
    filtered = digram_filter(filtered)
    view_by_letter(name, filtered)


def __prep_words(name):
    """Prep word list for finding anagrams."""
    words = load("words.txt")
    words = [word.lower() for word in words if len(word) == len(name)]
    return words


def __cv_map_words(name):
    """Map letters in words to consonants & vowels."""
    vowels = "aeiouy"
    words = __prep_words(name)
    cv_mapped_word = []
    for word in words:
        temp = ""
        for letter in word:
            temp += "v" if letter in vowels else "c"
        cv_mapped_word.append(temp)
    total = len(set(cv_mapped_word))
    excluded = int(total * 0.05)
    count_pruned = Counter(cv_mapped_word).most_common(total - excluded)
    filtered_cv_map = set()
    for pattern, _ in count_pruned:
        filtered_cv_map.add(pattern)
    print(f"length filtered_cv_map: {len(filtered_cv_map)}")
    return filtered_cv_map


def cv_map_filter(name):
    """Remove permutations of words based on unlikely cons-vowel combos."""
    perms = {"".join(i) for i in permutations(name)}
    filtered_cv_map = __cv_map_words(name)
    print(f"length of initial permutations set: {len(perms)}")
    vowels = "aeiouy"
    result = set()
    for candidate in perms:
        temp = ""
        for letter in candidate:
            if letter in vowels:
                temp += "v"
            else:
                temp += "c"
        if temp in filtered_cv_map:
            result.add(candidate)
    print(f"# choices after filter_1: {len(result)}")
    return result


def trigram_filter(words):
    """Remove unlikely trigrams from permutations."""
    trigrams_filtered = load("least-likely_trigrams.txt")
    result = set()
    for candidate in words:
        for triplet in trigrams_filtered:
            triplet = triplet.lower()
            if triplet in candidate:
                result.add(candidate)
    result = words - result
    print(f"# of choices after filter_2: {len(result)}")
    return result


def digram_filter(words):
    """Remove unlikely digrams from permutations."""
    rejects = [
        "dt",
        "lr",
        "md",
        "ml",
        "mr",
        "mt",
        "mv",
        "td",
        "tv",
        "vd",
        "vl",
        "vm",
        "vr",
        "vt",
    ]
    first_pair_rejects = [
        "ld",
        "lm",
        "lt",
        "lv",
        "rd",
        "rl",
        "rm",
        "rt",
        "rv",
        "tl",
        "tm",
    ]
    result = set()
    for candidate in words:
        for reject in rejects:
            if reject in candidate:
                result.add(candidate)
        for first_pair in first_pair_rejects:
            if candidate.startswith(first_pair):
                result.add(candidate)
    result = words - result
    print(f"# of choices after filter_3: {len(result)}")
    if "voldemort" in result:
        print("Voldemort found!", file=sys.stderr)
    return result


def view_by_letter(name, words):
    """Filter to anagrams starting with input letter."""
    print(f"Remaining letters: {name}")
    u_in = input("select a starting letter or press Enter to see all: ")
    subset = []
    for candidate in words:
        if candidate.startswith(u_in):
            subset.append(candidate)
    print(*sorted(subset), sep="\n")
    print(f"Number of choices starting with {u_in}: {len(subset)}")
    try_again = input("Try again? (Press Enter else any other key to Exit): ")
    if try_again.lower() == "":
        view_by_letter(name, words)
    else:
        sys.exit("Bye-bye!")


if __name__ == "__main__":
    main()
