#!/usr/bin/env python3

import sys

x = sys.argv[1:]

count = 0
if len(x) < 2:
    print("none")

else:
    for i in range(1, len(x)-1):
        if x[i] == x[0]:
            count +=1

    if count == 0:
        print("none")
    else:
        print(count)