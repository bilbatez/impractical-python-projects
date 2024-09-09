#!/usr/bin/env python3
import itertools

def sanitize_input(message):
    """Sanitize message"""
    return "".join(message.strip().split())

def decrypt(message):
    """Decrypt using rail fence cipher"""
    u_in = sanitize_input(message)
    row_1_len = int(len(u_in) / 2 + 1 if len(u_in) % 2 == 1  else len(u_in) / 2)
    res = []
    for row_1, row_2 in itertools.zip_longest(u_in[:row_1_len], u_in[row_1_len:]):
        res.append(row_1 + row_2)
    return "".join(res).strip().lower()

def main():
    """Main Program"""
    u_in = input("Input message to decrypt: ")
    print(decrypt(u_in))

if __name__ == "__main__":
    main()