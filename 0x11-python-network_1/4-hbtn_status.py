#!/usr/bin/python3
"""
Python script that fetches an URL with requests
"""
import requests


if __name__ == "__main__":
    rq = requests.get('https://alx-intranet.hbtn.io/status')
    txt = rq.text
    print('Body response:')
    print('\t- type: {}\n\t- content: {}'.format(type(txt), txt))
