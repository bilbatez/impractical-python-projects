#!/usr/bin/env python3
"""Fake Email Generator.

A simple unique fake email generator.

Author: Albert Julian Tannady <me@albertjtan.com>
"""

import os
import time
import random
import string
from datetime import datetime
import argparse

EMAIL_DOMAIN = [
    "gmail.com",
    "yahoo.com",
    "hotmail.com",
    "outlook.com",
    "ymail.com",
    "aol.com",
    "msn.com",
]

LETTERS = string.ascii_lowercase + "".join([str(num) for num in range(0, 10)])
DATE_PATTERN = "%d/%m/%Y %H:%M:%S"


def get_args():
    """Get command-line arguments."""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Fake Data Generator",
    )
    parser.add_argument(
        "-n",
        "--num",
        type=int,
        default=1000,
        help="Number of data needs to be generated",
    )
    parser.add_argument(
        "-of",
        "--output-filename",
        type=str,
        default=f"{time.time_ns()//1000}",
        help="Output filename",
    )
    parser.add_argument("-e",
                        "--extension",
                        type=str,
                        default=".txt",
                        help="Output File Extension")
    return parser.parse_args()


def main():
    """Run program."""
    print(r"""
____ ____ _  _ ____    ____ _  _ ____ _ _    
|___ |__| |_/  |___    |___ |\/| |__| | |    
|    |  | | \_ |___    |___ |  | |  | | |___ 
                                             
____ ____ _  _ ____ ____ ____ ___ ____ ____ 
| __ |___ |\ | |___ |__/ |__|  |  |  | |__/ 
|__] |___ | \| |___ |  \ |  |  |  |__| |  \     
    """)
    print("Created by: Albert JT\n")

    args = get_args()
    print(
        f"Start generating email!! [{datetime.now().strftime(DATE_PATTERN)}]")

    if not os.path.exists("./output"):
        os.makedirs("output")

    with open("./output/" + args.output_filename + args.extension,
              "at") as o_fh:
        created_emails = set()
        for _ in range(args.num):
            email = create_email()
            while email in created_emails:
                email = create_email()
            email += "\n"
            o_fh.write(email)
    print(f"Finish!! please check file:{args.output_filename} " +
          f"[{datetime.now().strftime(DATE_PATTERN)}]")


def create_email():
    """Create random email."""
    domain = random.choice(EMAIL_DOMAIN)
    name = "".join(
        [random.choice(LETTERS) for _ in range(random.randrange(9, 20))])
    return f"{name}@{domain}"


if __name__ == "__main__":
    main()
