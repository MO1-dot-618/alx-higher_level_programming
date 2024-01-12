#!/usr/bin/python3
"""listing states"""


import MySQLdb
import sys


def listing(username, password, db_name, name):
    """function to list states"""

    conn = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password,
        db=db_name, charset="utf8"
    )
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE CONVERT(name USING Latin1) \
    COLLATE Latin1_General_CS = %s ORDER BY id ASC"
    cur.execute(query, (name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    if (len(sys.argv)) == 5:
        listing(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
