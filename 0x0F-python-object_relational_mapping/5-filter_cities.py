#!/usr/bin/python3
"""This script lists cities"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    state_name = sys.argv[4]
    cur.execute(
        """SELECT cities.name FROM cities INNER JOIN states
        ON cities.state_id = states.id WHERE states.name = '{}'""".
        format(state_name))
    full = cur.fetchall()

    print(', '.join(x[0] for x in full))
