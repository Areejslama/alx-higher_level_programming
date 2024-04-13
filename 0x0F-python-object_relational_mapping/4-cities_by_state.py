#!/usr/bin/python3
"""this script list cities"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY id ASC")
    town = cur.fetchall()
    for i in town:
        print(i)
