#!/usr/bin/env python3
"""
Route Transposition Cipher Decoder Prototype

Author: Albert Julian Tannady <me@albertjtan.com>
"""
ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

cipherlist = list(ciphertext.split())

COLS = 4
ROWS = 5
key = "-1 2 -3 4"
translation_matrix = [None] * COLS
plaintext = ""
start = 0
stop = ROWS

key_int = [int(i) for i in key.split()]

for k in key_int:
    if k < 0:
        col_items = cipherlist[start:stop]
    elif k > 0:
        col_items = list(reversed(cipherlist[start:stop]))
    translation_matrix[abs(k) - 1] = col_items
    start += ROWS
    stop += ROWS

print(f"\nciphertext = {ciphertext}")
print("\ntranslation matrix = ", *translation_matrix, sep="\n")
print(f"\nkey length = {len(key_int)}")


for i in range(ROWS):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + " "

print(f"\nplaintext = {plaintext}")
