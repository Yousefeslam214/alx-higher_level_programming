#!/usr/bin/python3
for num in range(0, 100):
    if num < 10:
        print(f"0{num}, ",end="")
    elif num >= 10 and num < 99:
        print(f"{num}, ",end="")
    else:
        print(f"{num}")
