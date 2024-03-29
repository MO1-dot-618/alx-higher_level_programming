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
    query = "SELECT cities.name FROM cities \
    INNER JOIN states ON states.id = cities.state_id \
    WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(query, (name,))
    query_rows = cur.fetchall()
    print(", ".join(state[0] for state in query_rows))
    cur.close()
    conn.close()


if __name__ == "__main__":
    if (len(sys.argv)) == 5:
        listing(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
