#!/usr/bin/python3
'''This script lists a database'''

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=330)
curs = db.cursor()
curs.execute(
        "SELECT * FROM states;")
states = cursor.fetchall()
for s in states:
    print(s)
cursor.close()
db.close()
