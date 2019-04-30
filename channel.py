#!/usr/bin/env python3

channel = int(input("What channel do you REALLY want?: "))

if channel < 11:
    print("You need the basic package")
elif channel < 41:
    print("You need the standard package")
elif channel < 101:
    print("You need the premium package")
elif channel < 201:
    print("You need the HD package")

else:
    print("You need the Expensive package")


