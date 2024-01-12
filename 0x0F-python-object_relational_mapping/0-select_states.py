#!/usr/bin/python3
"""listing states"""


import MySQLdb
import sys


def listing(username, password, db_name):
    """function to list states"""

    conn = MySQLdb.connect(
        host="localhost", port=3306, user="root", passwd="root",
        db="hbtn_0e_0_usa", charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    if (len(sys.argv)) == 4:
        listing(sys.argv[1], sys.argv[2], sys.argv[3])
