"""delete data from table
"""
from mysql import connector

database_connection = connector.connect(
    host='localhost',
    user='salar',
    passwd="52212057",
    database='py_university'
)

cursor = database_connection.cursor()

# delete from students table
SQL = "DELETE FROM students WHERE average<=15"
cursor.execute(SQL)


database_connection.commit()
