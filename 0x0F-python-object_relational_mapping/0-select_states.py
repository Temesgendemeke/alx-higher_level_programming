#!/usr/bin/python3
import MySQLdb
import sys


arg = sys.argv
username = arg[1]
password = arg[2]
dbname = arg[3]

# The code should not be executed when imported
if __name__ == '__main__':
    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port = 3306, user=username, passwd=password, db=dbname)
    # It gives us the ability to have multiple seperate working environments
    # through the same connection to the database.
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()




