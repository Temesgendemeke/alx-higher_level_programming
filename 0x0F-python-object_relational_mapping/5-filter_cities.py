#!/usr/bin/python3
"""_summary_"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name  FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = '{}' ORDER BY cities.id ASC;".format(argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    j = []
    for i in rows:
        j.append(i[1])
    print(", ".join(j))
    cur.close()
    db.close()
