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
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="hbtn_0e_0_usa"
    )
mycursor = mydb.cursor()
mycursor.execute(" SELECT * FROM states order by  states.id ; ")
for i in mycursor:
    print(i)
