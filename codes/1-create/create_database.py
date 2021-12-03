"""connect to mysql server and create database
"""

# python -m pip install mysql-connector
from mysql import connector

# connection to sever
connection = connector.connect(
    host='localhost',
    user='salar',
    passwd="52212057"
)

# make cursor
cursor = connection.cursor()

# sql code
QUERAY = "CREATE DATABASE university"
# execute sql script
cursor.execute(QUERAY)

# show all database
QUERAY = "SHOW DATABASES"
cursor.execute(QUERAY)

for record in cursor:
    print(*record)
