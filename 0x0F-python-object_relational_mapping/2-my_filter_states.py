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
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * \
                FROM `states` \
                WHERE BINARY `name` = '{}'\
                    ORDER BY id ASC".format(sys.argv[4]))
    for states in c.fetchall():
        print(states)
    c.close()
    db.close()
