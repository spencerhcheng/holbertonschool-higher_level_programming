#!/usr/bin/python3
'''
Lists all cities by state from the database hbtn_0e_4_usa
'''
import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT cities.name\
              FROM cities JOIN states ON states.id=cities.state_id\
              WHERE BINARY states.name = '{}'\
              ORDER BY cities.id ASC".format(sys.argv[4]))
    rows = c.fetchall()
    result = []
    for x in rows:
        result.append(x[0])
    print (', '.join(result))
    c.close()
    db.close()
