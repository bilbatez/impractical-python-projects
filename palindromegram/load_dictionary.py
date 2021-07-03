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


def load(file):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            return [word.lower() for word in loaded_txt]
    except IOError as ex:
        print(f"{ex}\nError opening {file}. Terminating program.", file=sys.stderr)
        sys.exit()
