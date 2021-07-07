#!/usr/bin/env python3
"""Decrypt a path through a Union Route Cipher.

Designed for whole-word transposition ciphers with variable rows & columns.
Assumes encryption began at either top or bottom of a column.
Key indicates the order to read columns and the direction to traverse.
Negative column numbers mean start at bottom and read up.
Positive column numbers mean start at top & read down.


Example below is for 4x4 matrix with key -1 2 -3 4.
Note "0" is not allowed.
Arrows show encryption route; for negative key values read UP.

  1   2   3   4
 ___ ___ ___ ___
| ^ | | | ^ | | | MESSAGE IS WRITTEN
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | ACROSS EACH ROW
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | IN THIS MANNER
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | LAST ROW IS FILLED WITH DUMMY WORDS
|_|_|_v_|_|_|_v_|
START        END

Required inputs - a text message, # of columns, # of rows, key string

Prints translated plaintext

"""

import sys


class State:
    """User inputs."""

    def __init__(self):
        """User can change values here."""
        self.ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19".split()
        self.cols = 4
        self.rows = 5
        self.key = [int(x) for x in "-1 2 -3 4".split()]

    def print_state_info(self):
        """Print user input summary."""
        print(f"\nCiphertext = {self.ciphertext}")
        print(f"Trying {self.cols} columns")
        print(f"Trying {self.rows} rows")
        print(f"Trying key = {self.key}")

    def validate_state(self) -> None:
        """Validate all user input."""
        self.__validate_col_row()
        self.__validate_key()

    def __validate_col_row(self) -> None:
        """Check that input columns & rows are valid vs. message length."""
        factors = []
        len_cipher = len(self.ciphertext)
        for i in range(2, len_cipher):
            if len_cipher % i == 0:
                factors.append(i)

        print(f"\nLength of cipher = {len_cipher}")
        print(f"Acceptable column/row values include: {factors}")
        print()

        if self.rows * self.cols != len_cipher:
            print(
                "\nError - Input columns & rows not factors of length of cipher. "
                "Terminating program.",
                file=sys.stderr,
            )
            sys.exit(1)

    def __validate_key(self) -> None:
        """Check key validity."""
        min_key = min(self.key)
        max_key = max(self.key)
        if (
            len(self.key) != self.cols
            or min_key < -self.cols
            or max_key > self.cols
            or 0 in self.key
        ):
            print("\nError - Problem with key. Terminating.", file=sys.stderr)
            sys.exit(1)

    def decrypt(self):
        """Decrypt message."""
        translation_matrix = self.__build_matrix()
        plaintext = ""
        for _ in range(self.rows):
            for matrix_col in translation_matrix:
                word = str(matrix_col.pop())
                plaintext += word + " "
        return plaintext

    def __build_matrix(self):
        """Turn every n items in a list into a new item in a list of lists."""
        translation_matrix = [None] * self.cols
        start = 0
        stop = self.rows
        for k in self.key:
            if k < 0:
                col_items = self.ciphertext[start:stop]
            elif k > 0:
                col_items = list(reversed(self.ciphertext[start:stop]))
            translation_matrix[abs(k) - 1] = col_items
            start += self.rows
            stop += self.rows
        return translation_matrix


def main():
    """Run program and print decrypted plaintext."""
    state = State()
    state.print_state_info()
    state.validate_state()
    plaintext = state.decrypt()
    print(f"Plaintext = {plaintext}")


if __name__ == "__main__":
    main()
