#!/usr/bin/python3
'''
Lists all states from the database hbtn_0e_0_usa
'''
import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT states.id, states.name\
              FROM states ORDER BY states.id ASC")
    rows = c.fetchall()
    for x in rows:
        print(x)
    c.close()
    db.close()
