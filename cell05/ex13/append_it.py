#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("none")
else:
    for i in sys.argv[1:]:
        if len(i) >= 3 and i[-3:] == "ism":
            pass
        else:
            print(f"{i}ism")