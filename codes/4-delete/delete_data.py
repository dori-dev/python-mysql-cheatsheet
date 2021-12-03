"""delete data from table
"""
from mysql import connector

database_connection = connector.connect(
    host='localhost',
    user='user',
    passwd="password",
    database='university'
)

cursor = database_connection.cursor()

# delete from students table
SQL = "DELETE FROM students WHERE average<=15"
cursor.execute(SQL)


database_connection.commit()
