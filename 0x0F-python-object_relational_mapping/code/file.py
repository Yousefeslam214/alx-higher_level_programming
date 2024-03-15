#!/usr/bin/python3
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
        #database="HR_Databases"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES;")
    databases = mycursor.fetchall()
    if databases:
        print("List of databases:")
        for db in databases:
            print(db[0])
    else:
        print("No databases found.")
except mysql.connector.Error as err:
    print("Error:", err)
