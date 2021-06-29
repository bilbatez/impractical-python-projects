#!/usr/bin/env python3
"""
Pig Latin Unit Test
Author: Albert Julian Tannady <me@albertjtan.com>
"""
from string import punctuation
from piglatinify import convert


def test_convert_single_vowel():
    """test convert a single vowel"""
    for vowel in "aeiou":
        result = convert(vowel)
        assert result == vowel + "way"


def test_convert_single_consonant():
    """test convert a single consonant"""
    result = convert("b")
    assert result == "b"


def test_convert_noun():
    """test convert 'noun' word"""
    result = convert("noun")
    assert result == "ounnay"


def test_convert_adjective():
    """test convert 'adjective' word"""
    result = convert("adjective")
    assert result == "adjectiveway"


def test_convert_word_with_numbers():
    """test convert word with numbers"""
    for word in ["1", "a1", "1a"]:
        assert convert(word) == word


def test_convert_punctuations():
    """test convert punctuation"""
    for c in punctuation:
        assert convert(c) == c


def test_convert_punctuations():
    """test convert punctuations"""
    assert convert("(*-*)") == "(*-*)"


def test_convert_with_blank_input():
    """test convert with blank input"""
    assert convert("") == ""
