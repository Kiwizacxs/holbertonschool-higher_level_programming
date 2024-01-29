#!/usr/bin/python3
for x in range(0, 99):
    if x < 10:
        print("0", end="")
    print(x, end=", ")
x += 1
print(x)
