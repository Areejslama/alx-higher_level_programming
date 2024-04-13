#!/usr/bin/python3
'''this script list a database'''

import MySQLdb
import sys
db = MySQLdb.connect(
        user = sys.argv[1], passwd = sys.argv[2], db = sys.argv[3], port = 3306)
cursor = db.cursor()
cursor.execute("SELECT * FROM states;")
state= cursor.fetchall()
for s in state:
    print(s)
