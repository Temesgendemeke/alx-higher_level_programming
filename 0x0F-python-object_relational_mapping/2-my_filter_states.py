#!/usr/bin/python3
"""_summary_"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name={} ORDER BY states.id ASC".format(argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
