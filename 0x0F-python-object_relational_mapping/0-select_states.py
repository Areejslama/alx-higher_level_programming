#!/usr/bin/python3
'''This script lists a database'''

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
cursur = db.cursor()
cursur.execute("SELECT * FROM states;")
states = cursor.fetchall()
for s in states:
    print(s)
