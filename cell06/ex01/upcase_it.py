#!/usr/bin/env python3
import sys

def upcase_it(x):
    return x.upper()

if len(sys.argv) < 2:
    pass
else:
    for arg in sys.argv[1:]:
        print(upcase_it(arg))