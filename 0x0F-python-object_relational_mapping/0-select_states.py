#!/usr/bin/python3
import MySQLdb
import sys


arg = sys.argv
username = arg[1]
password = arg[2]
dbname = arg[3]

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port = 3306, user=username, passwd=password, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT * FROM FROM hbtn_0e_0_usa.states ORDER BY states.id")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()




