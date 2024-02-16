#!/usr/bin/python3
"""_summary_"""

if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
