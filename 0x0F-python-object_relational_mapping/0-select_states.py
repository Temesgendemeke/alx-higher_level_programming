#!/usr/bin/python3
"""_summary_"""

import MySQLdb
import sys

# The code should not be executed when imported
if __name__ == '__main__':
    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port = 3306, user= sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # It gives us the ability to have multiple seperate working environments
    # through the same connection to the database.
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()




