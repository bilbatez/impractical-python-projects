#!/usr/bin/env python3
MAX_GROUP_NUMBER = 5

def sanitize_input(message):
    """Sanitize message"""
    return "".join(message.split()).upper()

def encrypt(message):
    """Encrypt using rail fence cipher"""
    u_in = sanitize_input(message)

    res = [None] * len(u_in)
    res = u_in[::2] + u_in[1::2]
    res = [res[i:i+MAX_GROUP_NUMBER] for i in range(0, len(res), MAX_GROUP_NUMBER)]
    return " ".join(res)
   
def main():
    u_in = input("Input message to encrypt: ")
    print(encrypt(u_in))

if __name__ == "__main__":
    main()