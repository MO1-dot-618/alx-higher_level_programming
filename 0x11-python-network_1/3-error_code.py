#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request and handles
errors"""

from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as erar:
        print('Error code: {}'.format(erar.code))
