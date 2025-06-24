#!/usr/bin/env python3

x = 0
y = 0
index = 11
now = 0
while x <=10:
    print(f"Table de  {x}:",end=" ")
    while now < index:
        print(y, end=" ")
        now += 1
        y += x
    print()
    now = 0
    y= 0
    x+=1
