#!/usr/bin/python3
import MySQLdb
import sys


arg = sys.argv
username = arg[1]
password = arg[2]
dbname = arg[3]

db = MySQLdb.connect(host="localhost", port = 3306, user=username, passwd=password, db=dbname, charset="utf8")
cur = db.cursor()

cur.execute("SELECT * FROM FROM hbtn_0e_0_usa.states ORDER BY states.id")

db.close()




