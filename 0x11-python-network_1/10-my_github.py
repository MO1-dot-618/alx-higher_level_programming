#!/usr/bin/python3
"""script that takes GitHub credentials"""

import requests
import sys

if __name__ == "__main__":
    username = "MO1-dot-618"
    password = ("github_pat_11APSOIYA0bgvaQZf1smzQ_CEk2A9cvxJpoe35kN"
                "7qCsTKg9PoxiGQdiLEEMD4Mwmn57D4CDGZwP9o1MkW")
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get('id'))
    else:
        print("None")
