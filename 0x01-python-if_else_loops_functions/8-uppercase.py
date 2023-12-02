#!/usr/bin/python3
def uppercase(letter):
    for i in letter:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print()
