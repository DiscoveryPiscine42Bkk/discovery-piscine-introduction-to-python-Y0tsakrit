#!/usr/bin/env python3

import sys
from checkmate import checkmate

def main():

    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            try:
                board = open(arg, "r").read()
                checkmate(board)
            except:
                print("Error: file cannot be read")

if __name__ == "__main__":
    main()
