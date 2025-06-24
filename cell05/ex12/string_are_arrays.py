#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("none", end="")
else:
    check = False
    for arg in sys.argv[1:]:  
        for char in arg:     
            if char == "z":
                print("z", end="")
                check = True
    
    if not check:
        print("none", end="")