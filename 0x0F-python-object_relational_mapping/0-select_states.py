#!/usr/bin/python3
"""Lists all states from database hbtn_0e_0_usa."""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Connect to db."""
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        port=3306,
        database=argv[3],
    )
    cur = db.cursor()

    # execute query
    cur.execute("SELECT * FROM states ORDER BY id ASC;")

    result = cur.fetchall()

    for row in result:
        print(row)

    # close db connection
    cur.close()
    db.close()
