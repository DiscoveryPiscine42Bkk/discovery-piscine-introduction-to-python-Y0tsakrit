#!/usr/bin/env python3

x = [2, 8, 9, 48, 8, 22, -12, 2]
y=[]
print(x)
for i in x:
    if i > 5:
        y.append(i+2)
print(set(y))
