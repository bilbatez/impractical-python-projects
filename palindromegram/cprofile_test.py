#!/usr/bin/env python3
"""cprofile test for palindrome and palingram programs.

Author: Albert Julian Tannady <me@albertjtan.com>
"""

import cProfile
import palindrome
import palingram

#Palindrome program.
cProfile.run("palindrome.find_palindromes()")
#Recusive palindrome program.
cProfile.run("palindrome.find_palindromes_recursively()")

#Palingram program.
cProfile.run("palingram.find_palingrams()")
