#!/usr/bin/env python3

import os

def find_all(path):
    result =[]
    for root, dirs, files in os.walk(path):
   
        return result

lookfor = input("Enter a path to search: ")

print(find_all(lookfor))
