"""Insert many values to database tables
"""
from mysql import connector

database_connection = connector.connect(
    host='localhost',
    user='user',
    passwd='password',
    database='university'
)

cursor = database_connection.cursor()

# insert to faculty table
SQL = """
INSERT INTO faculty(
    faculty_ID,
    name,
    admin,
    fundation_year,
    address
)
VALUES(%s, %s, %s, %s, %s)
"""

# insert value
value = (1, 'computer', 'Dr Dori', '1390', 'tehran')
cursor.execute(SQL, value)

# insert many values
values = [
    (2, 'electronic', 'Dr Mohammady', '1390', 'shiraz'),
    (3, 'mathematics', 'Dr Karimi', '1400', 'isfahan'),
    (4, 'architecture', 'Mr Akbari', '1399', 'tabriz'),
    (5, 'data science faculty', 'Dr Dori', '1390', 'mashhad')
]
cursor.executemany(SQL, values)


# for change in database values
database_connection.commit()
