from mysql import connector

database_connection = connector.connect(
    host='localhost',
    user='user',
    passwd='password',
    database='university'
)

cursor = database_connection.cursor()


# faculty
print('--------------- Faculty Data---------------')
SQL = """
SELECT * FROM faculty
"""
cursor.execute(SQL)

# fetchall all result from database
result = cursor.fetchall()

for record in result:
    print(record)


# students
print('--------------- Students Data---------------')
SQL = """
SELECT * FROM students
"""
cursor.execute(SQL)
result = cursor.fetchall()

for record in result:
    print(record)


# field
print('--------------- Field Data---------------')
SQL = """
SELECT * FROM field
"""
cursor.execute(SQL)
result = cursor.fetchall()

for record in result:
    print(record)


# professors
print('--------------- professors Data---------------')
SQL = """
SELECT * FROM professors
"""
cursor.execute(SQL)
result = cursor.fetchall()

for record in result:
    print(record)
