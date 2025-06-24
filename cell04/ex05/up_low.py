#!/usr/bin/env python3

import sys


for i in sys.argv[1:]:
    if i.isupper():
        print(i.lower(), end="")
    elif i.islower():
        print(i.upper(), end="")
    else:
        print(i, end="")