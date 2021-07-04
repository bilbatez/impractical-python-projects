#!/usr/bin/env python3
"""Test anagram functionality."""

from anagrams import find_anagrams

def test_anagram():
    """Test anagram functionalities."""
    anagrams = find_anagrams("Foster")
    expected = ["fetors", "forest", "fortes", "foster", "softer"]
    for i in range(len(anagrams)):
        assert anagrams[i] == expected[i]
        