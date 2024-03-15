#!/usr/bin/python3
import mysql.connector

import MySQLdb
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hbtn_0e_0_usa"
)
mycursor = mydb.cursor()
mycursor.execute(" SELECT * FROM states; ")
for i in mycursor:
    print(i)
