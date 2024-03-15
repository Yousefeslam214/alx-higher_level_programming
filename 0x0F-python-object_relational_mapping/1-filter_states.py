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
    c.execute("SELECT * FROM states ORDER BY id ASC")
    for states in c.fetchall():
        if states[1][0] == 'N':
            print(states) 
    c.close()
    db.close()
