#!/usr/bin/env python3

import sys

x = sys.argv[1:]

if len(x) == 0:
    print("none")
else:
    y= input("What was the parameter? ")
    if x== y:
        print("Good job!")
    else:
        print("Nope, sorry...")