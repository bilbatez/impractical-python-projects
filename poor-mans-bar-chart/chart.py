#!/usr/bin/env python3
"""
Poor Man's Bar Chart

Author: Albert Julian Tannady <me@albertjtan.com>
"""

import sys
from string import ascii_lowercase as ALPHABETS


def welcome():
    """Greeting"""
    print(r"""
  ___                __  __           _      ___              ___ _             _   
 | _ \___  ___ _ _  |  \/  |__ _ _ _ ( )___ | _ ) __ _ _ _   / __| |_  __ _ _ _| |_ 
 |  _/ _ \/ _ \ '_| | |\/| / _` | ' \|/(_-< | _ \/ _` | '_| | (__| ' \/ _` | '_|  _|
 |_| \___/\___/_|   |_|  |_\__,_|_||_| /__/ |___/\__,_|_|    \___|_||_\__,_|_|  \__|
                                                                                    
    """)
    print("Created by: Albert JT")


def main():
    """Main Program"""
    welcome()
    print()
    while True:
        counters = {}
        u_in = input("Input sentence to display graph! [q to Quit]: ").lower()
        if u_in == "q":
            sys.exit("Bye-bye!")

        print("Chart:")
        for char in u_in:
            if char in ALPHABETS:
                counters[char] = counters.get(char, 0) + 1

        for char in ALPHABETS:
            if counters.get(char, 0):
                print(f"{char}: {convert(char, counters)}")
        print()


def convert(char, counters):
    """Convert counters to graphical chart"""
    return "".join(["#" for _ in range(counters.get(char, 0))])


if __name__ == "__main__":
    main()
