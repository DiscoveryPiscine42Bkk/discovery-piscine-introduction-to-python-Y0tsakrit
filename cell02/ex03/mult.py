#!/usr/bin/env python3

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

result = num_1 * num_2

print(f"{num_1} x {num_2} = {result}")

if result > 0:
    print("This number is positive.")
elif result < 0:
    print("This number is negative.")
else:
    print("This number is positive and negative.")