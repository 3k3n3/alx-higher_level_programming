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
    query = """
        SELECT * FROM states WHERE BINARY name='{}' ORDER BY id ASC;
        """.format(argv[4])
    cur.execute(query)

    result = cur.fetchall()

    for row in result:
        print(row)

    # Close DB connections
    cur.close()
    db.close()
