#!/usr/bin/env python3
"""
Silly Name Generator
Author: Albert Julian Tannady <me@albertjtan.com>
"""

import sys
import time
import random

FIRST_NAMES = [
    "Baby Oil",
    "Bad News",
    "Big Burps",
    "Bill 'Beenie-Weenie'",
    "Bob 'Stinkbug'",
    "Bowel Noises",
    "Boxelder",
    "Bud 'Lite'",
    "Butterbean",
    "Buttermilk",
    "Buttocks",
    "Chad",
    "Chesterfield",
    "Chewy",
    "Chigger",
    "Cinnabuns",
    "Cleet",
    "Cornbread",
    "Crab Meat",
    "Crapps",
    "Dark Skies",
    "Dennis Clawhammer",
    "Dicman",
    "Elphonso",
    "Fancypants",
    "Figgs",
    "Foncy",
    "Gootsy",
    "Greasy Jim",
    "Huckleberry",
    "Huggy",
    "Ignatious",
    "Jimbo",
    "Joe 'Pottin Soil'",
    "Johnny",
    "Lemongrass",
    "Lil Debil",
    "Longbranch",
    '"Lunch Money"',
    "Mergatroid",
    '"Mr Peabody"',
    "Oil-Can",
    "Oinks",
    "Old Scratch",
    "Ovaltine",
    "Pennywhistle",
    "Pitchfork Ben",
    "Potato Bug",
    "Pushmeet",
    "Rock Candy",
    "Schlomo",
    "Scratchensniff",
    "Scut",
    "Sid 'The Squirts'",
    "Skidmark",
    "Slaps",
    "Snakes",
    "Snoobs",
    "Snorki",
    "Soupcan Sam",
    "Spitzitout",
    "Squids",
    "Stinky",
    "Storyboard",
    "Sweet Tea",
    "TeeTee",
    "Wheezy Joe",
    "Winston 'Jazz Hands'",
    "Worms",
]

LAST_NAMES = [
    "Appleyard",
    "Bigmeat",
    "Bloominshine",
    "Boogerbottom",
    "Breedslovetrout",
    "Butterbaugh",
    "Clovenhoof",
    "Clutterbuck",
    "Cocktoasten",
    "Endicott",
    "Fewhairs",
    "Gooberdapple",
    "Goodensmith",
    "Goodpasture",
    "Guster",
    "Henderson",
    "Hooperbag",
    "Hoosenater",
    "Hootkins",
    "Jefferson",
    "Jenkins",
    "Jingley-Schmidt",
    "Johnson",
    "Kingfish",
    "Listenbee",
    "M'Bembo",
    "McFadden",
    "Moonshine",
    "Nettles",
    "Noseworthy",
    "Olivetti",
    "Outerbridge",
    "Overpeck",
    "Overturf",
    "Oxhandler",
    "Pealike",
    "Pennywhistle",
    "Peterson",
    "Pieplow",
    "Pinkerton",
    "Porkins",
    "Putney",
    "Quakenbush",
    "Rainwater",
    "Rosenthal",
    "Rubbins",
    "Sackrider",
    "Snuggleshine",
    "Splern",
    "Stevens",
    "Stroganoff",
    "Sugar-Gold",
    "Swackhamer",
    "Tippins",
    "Turnipseed",
    "Vinaigrette",
    "Walkingstick",
    "Wallbanger",
    "Weewax",
    "Weiners",
    "Whipkey",
    "Wigglesworth",
    "Wimplesnatch",
    "Winterkorn",
    "Woolysocks",
]


def welcome():
    """Print greetings"""
    print(r"""
   _____ _ ____         _   __                        
  / ___/(_) / /_  __   / | / /___ _____ ___  ___      
  \__ \/ / / / / / /  /  |/ / __ `/ __ `__ \/ _ \     
 ___/ / / / / /_/ /  / /|  / /_/ / / / / / /  __/     
/____/_/_/_/\__, /  /_/ |_/\__,_/_/ /_/ /_/\___/      
  / ____/__/____/  ___  _________ _/ /_____  _____    
 / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/    
/ /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /        
\____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/ 
""")
    print("Generating stupid names since 2021")
    print("Created by: Albert JT")
    print("----------------------------------")
    time.sleep(1)


def main():
    """Main Program"""
    welcome()
    while True:
        print("You have been bestowed the named...")
        print(
            random.choice(FIRST_NAMES) + " " + random.choice(LAST_NAMES),
            file=sys.stderr, end="\n\n"
        )
        user_input = input("Try again? [y/n]: ").lower()
        print()
        if user_input not in "yn":
            print("Please input y or n!", end="\n\n")
        elif user_input == "n":
            sys.exit("Bye!!")


if __name__ == "__main__":
    main()
