#!/usr/bin/env python3

import requests

def main():
    r = requests.get('http://api.open-notify.org/astros.json')
    print(r.json())
    print('\n\n\n')

    print(r.json().get('people'))
main()
