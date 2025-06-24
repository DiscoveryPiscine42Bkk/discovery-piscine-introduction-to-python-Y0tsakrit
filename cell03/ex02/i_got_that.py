#!/usr/bin/env python3

x = input("What you gotta say? : ")

if x != "STOP":
    while True :
        x = input("I got that! Anything else? : ")
        if x == "STOP":
            break