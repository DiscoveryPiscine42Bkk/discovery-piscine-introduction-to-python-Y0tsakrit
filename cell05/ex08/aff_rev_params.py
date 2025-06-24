#!/usr/bin/env python3

x = input().split()

if len(x) < 2:
    print("none")

else:
    for i in range(len(x)-1,-1,-1):
        print(x[i])
    