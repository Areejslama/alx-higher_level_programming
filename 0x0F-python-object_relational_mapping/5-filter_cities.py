#!/usr/bin/python3
"""This script lists cities"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    state_name = sys.argv[4]
    cur.execute('''
        SELECT cities.id, cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    ''', (state_name,))
    towns = cur.fetchall()
    for i in towns:
        print(i)