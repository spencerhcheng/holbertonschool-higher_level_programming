#!/usr/bin/python3
'''
Takes in an argument and displays
all values in te states table of hbtn_0e_0_usa
'''
import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT states.id, states.name\
              FROM states WHERE BINARY states.name=%s\
              ORDER BY states.id ASC", (sys.argv[4],))
    rows = c.fetchall()
    for x in rows:
        print(x)
    c.close()
    db.close()
