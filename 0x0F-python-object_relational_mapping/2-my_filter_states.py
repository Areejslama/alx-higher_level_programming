#!/usr/bin/python3
"""this script list states"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    name = "SELECT * FROM states WHERE name LIKE BINARY '{}%'"
    city = sys.argv[4]
    state = name.format(city)
    cur.execute(state)
    town = cur.fetchall()
    for i in town:
        print(i)
