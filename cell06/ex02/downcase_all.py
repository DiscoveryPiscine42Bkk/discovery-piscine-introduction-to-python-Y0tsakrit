#!/usr/bin/env python3
import sys

def downcase_it(x):
    return x.lower()

if len(sys.argv) < 2:
    pass
else:
    for arg in sys.argv[1:]:
        print(downcase_it(arg))