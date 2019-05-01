#!/usr/bin/env python3
'''
loopy test
'''
#channel = int(input("What channel do you REALLY want?: "))
FAVS = [26, 52, 4, 498, 102]
for channel in FAVS:
    if channel < 11:
        print("For Channel ", channel, "  You need the basic package")
    elif channel < 41:
        print("For Channel ", channel, "  You need the standard package")
    elif channel < 101:
        print("For Channel ", channel, "  You need the premium package")
    elif channel < 201:
        print("For Channel ", channel, "  You need the HD package")

    else:
        print("For Channel ", channel, "  You need the Expensive package")
