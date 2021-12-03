"""insert many values to database tables
"""
from mysql import connector

# TODO insert too many data


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
value = (1, 'computer', 'Dr Dori', '1390', 'Tehran')
cursor.execute(SQL, value)

# insert many values
values = [
    (2, 'electronic', 'Dr Mohammadi', '1390', 'Isfahan'),
    (3, 'mathematics', 'Dr Karimi', '1400', 'Shiraz'),
    (4, 'architecture', 'Mr Akbari', '1399', 'Tehran'),
    (6, 'data science', 'Mr Shahmoradi', '1390', 'Mashhad'),
    (7, 'chemistry', 'Dr Sharifi', '1390', 'Tehran'),
]
cursor.executemany(SQL, values)


# insert to field table
SQL = """
INSERT INTO faculty(
    field_ID,
    field_name,
    orientation,
    grade,
    faculty_ID
)
VALUES(%s, %s, %s, %s, %s)
"""

values = [
    (1, 'computer', 'software', 'bachelor', 1),
    (2, 'computer', 'hardware', 'bachelor', 1),
    (3, 'computer', 'maching learning', 'master', 6),
    (4, 'mathematics', 'pure mathematics', 'bachelor', 3),
    (5, 'art', '3D', 'master', 4),
    (6, 'electronic', 'robotic', 'master', 2),
    (7, 'data science', 'image processing', 'bachelor', 6),
    (8, 'computer', 'parallel processing', 'master', 1),
    (9, 'chemistry', 'pure chemistry', 'bachelor', 7),
]

cursor.executemany(SQL, values)


# insert to professors table
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
cursor.executemany(SQL, values)


# insert to students table
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
cursor.executemany(SQL, values)


# for save changes in database
database_connection.commit()
