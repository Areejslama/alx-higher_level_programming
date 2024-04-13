#!/usr/bin/python3
'''This script lists a database'''

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
curs = db.cursor()
curs.execute("SELECT * FROM states;")
state = cursor.fetchall()
for s in state:
    print(s)
cursor.close()
db.close()
