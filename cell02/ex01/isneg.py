#!/usr/bin/env python3

import sys


num = int(sys.argv[1])

if num > 0:
    print("This number is positive.")
elif num < 0:
    print("This number is negative.")
else:
    print("This number is both positive and negative.")