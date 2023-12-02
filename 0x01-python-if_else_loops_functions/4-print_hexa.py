#!/usr/bin/python3
"""Print the alphabet in lowercase, not followed by a new line."""

for letter in range(0, 99):
    hex_num = hex(letter)
    print(f"{letter} = {hex_num}")
