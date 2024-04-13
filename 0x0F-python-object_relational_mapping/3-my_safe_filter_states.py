#!/usr/bin/python3
"""This script lists states"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    name = "SELECT * FROM states WHERE name LIKE BINARY %s"
    city = sys.argv[4] + "%"
    cur.execute(name, (city,))
    towns = cur.fetchall()
    for town in towns:
        print(town)
