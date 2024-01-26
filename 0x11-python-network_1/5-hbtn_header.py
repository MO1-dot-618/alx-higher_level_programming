#!/usr/bin/python3
"""
Python script that sends a request to the URL and
displays variable value in header
"""
import requests
import sys


if __name__ == "__main__":
    try:
        rq = requests.get(sys.argv[1])
        print(rq.headers['X-Request-Id'])
    except Exception as e:
        pass
