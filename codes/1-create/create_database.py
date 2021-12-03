"""connect to mysql server and create database
"""
from mysql import connector

# connection to sever
connection = connector.connect(
    host='localhost',
    user='user',
    passwd="password"
)

# make cursor
cursor = connection.cursor()

# sql code
SQL = "CREATE DATABASE university"

# execute sql script
cursor.execute(SQL)

# show all database
SQL = "SHOW DATABASES"
cursor.execute(SQL)

for record in cursor:
    print(*record)
