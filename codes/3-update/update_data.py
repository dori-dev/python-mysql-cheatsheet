"""update data from table
"""
from mysql import connector

database_connection = connector.connect(
    host='localhost',
    user='user',
    passwd="password",
    database='university'
)

cursor = database_connection.cursor()

# update students table
SQL = """
UPDATE students
SET entering_year = entering_year-1
WHERE field_ID=1
"""
cursor.execute(SQL)

database_connection.commit()
