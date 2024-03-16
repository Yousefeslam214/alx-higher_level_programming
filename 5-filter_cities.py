#!/usr/bin/python3
"""
script that lists all states
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys
if __name__ == '__main__':
    """
    Access to the database
    """
    i = 0
    db = MySQLdb.connect(user=sys.argv[1], passwd='', db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT DISTINCT cities.name   FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name LIKE '{}'".format(sys.argv[4]))
    cities = c.fetchall()
    city_names = ", ".join(city[0] for city in cities)
    print(city_names)
    c.close()
    db.close()
