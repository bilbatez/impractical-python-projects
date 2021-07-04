"""Load a text file as a list.

Arguments:
-text file name (and directory path, if needed)

Exceptions:
-IOError if filename not found.

Returns:
-A list of all words in a text file in lower case.

Requires-import sys
"""

import sys


def load(filename):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            words = in_file.read().strip().split("\n")
            return [word.lower() for word in words]
    except IOError as ex:
        print(f"{ex}\nError opening {filename}. Terminating program.", file=sys.stderr)
        sys.exit()
