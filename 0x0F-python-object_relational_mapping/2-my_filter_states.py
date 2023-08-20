#!/usr/bin/python3
"""Returns all values that match argument(takes input) from hntn_0e_0_usa."""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    """Conections to server and execution script."""
    db = MySQLdb.connect(
            user=argv[1],
            port=3306,
            host="localhost",
            password=argv[2],
            db=argv[3],
    )
    cur = db.cursor()

    # Exucute query & fetch results
    cur.execute(f"SELECT * FROM states WHERE name='{argv[4]}' ORDER BY id ASC")
    result = cur.fetchall()

    for row in result:
        print(row)

    # Close DB connections
    cur.close()
    db.close()
