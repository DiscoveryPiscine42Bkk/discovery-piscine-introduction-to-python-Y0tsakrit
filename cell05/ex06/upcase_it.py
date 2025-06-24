#!/usr/bin/env python3

x = input().split()

if len(x) == 0:
    print("none")

else:
    for i in x:
        print(i.upper(), end=' ')
    