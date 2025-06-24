#!/usr/bin/env python3

import sys

if len(sys.argv) == 0:
    print("none")

else:
    for i in sys.argv:
        print(i.lower(), end=' ')
    