#!/usr/bin/env python3

num = int(input())

if num > 25:
    print("Error")
else:
    for i in range(num,26):
        print(f"Inside the loop, my variable is {i}")