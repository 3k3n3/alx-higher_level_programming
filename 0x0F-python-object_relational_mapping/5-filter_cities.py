#!/usr/bin/python3
"""Returns all cities of state provided as argument from hntn_0e_0_usa."""


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
    cur.execute("""
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id=states.id
        WHERE states.name=%(state)s
        ORDER BY states.id ASC; 
        """,{'state': argv[4]})
    result = cur.fetchall()
    
    # print in requested format
    print(", ".join([i[0] for i in result]))

    # Close DB connections
    cur.close()
    db.close()
