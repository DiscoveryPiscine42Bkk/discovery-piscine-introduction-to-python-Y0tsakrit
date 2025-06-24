#!/usr/bin/env python3

import sys

x = sys.argv[1:]

if len(x) < 2:
    print("none")

else:
    for i in range(len(x)-1,-1,-1):
        print(x[i])
    