#!/usr/bin/python3

import sys
if __name__ == "__main__":
    i = 0
    print("{} arguments:".format(len(sys.argv) - 1))
    for x in sys.argv:
        if x != sys.argv[0]:
            print("{}: {}".format(i, x))
        i += 1
