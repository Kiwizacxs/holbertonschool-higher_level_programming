#!/usr/bin/python3

import sys
if __name__ == "__main__":
    i = 0
    if len(sys.argv) == 1:
        print("0")
    else:
        for x in sys.argv:
            if x != sys.argv[0]:
                i = i + int(x)
        print(i)
