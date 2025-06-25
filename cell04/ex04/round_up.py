#!/usr/bin/env python3

num = float(input("Give me a number: "))
if num % 1 == 0:
    print(round(num))
else:
    print(int((num//1 )+1))