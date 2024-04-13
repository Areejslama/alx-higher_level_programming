#!/usr/bin/python3
"""this script list states with name"""
import sys
import MySQLdb

if  __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    city = cur.fetchall()
    for i in city:
        print(city)
