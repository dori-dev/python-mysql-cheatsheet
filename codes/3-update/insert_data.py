"""insert many values to database tables
"""
from mysql import connector

database_connection = connector.connect(
    host='localhost',
    user='user',
    passwd='password',
    database='university'
)

cursor = database_connection.cursor()

# -------------------- insert to faculty table --------------------
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
    (3, 'mathematics', 'Dr Karimi', '1380', 'Shiraz'),
    (4, 'architecture', 'Mr Akbari', '1399', 'Tehran'),
    (5, 'data science', 'Mr Shahmoradi', '1400', 'Mashhad'),
    (6, 'chemistry', 'Dr Sharifi', '1395', 'Tehran'),
]
cursor.executemany(SQL, values)


# -------------------- insert to field table --------------------
SQL = """
INSERT INTO field(
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
    (3, 'computer', 'maching learning', 'master', 5),
    (4, 'mathematics', 'pure mathematics', 'bachelor', 3),
    (5, 'art', '3D', 'master', 4),
    (6, 'electronic', 'robotic', 'master', 2),
    (7, 'data science', 'image processing', 'bachelor', 5),
    (8, 'computer', 'parallel processing', 'master', 1),
    (9, 'chemistry', 'pure chemistry', 'bachelor', 6),
]

cursor.executemany(SQL, values)


# -------------------- insert to professors table --------------------
SQL = """
INSERT INTO professors(
    name,
    family,
    degree,
    faculty_member,
    faculty_ID,
    phone,
    address
)
VALUES(%s, %s, %s, %s, %s, %s, %s)
"""

values = [
    ('Mohammad', 'Dori', 'dr', 1, 1, '09013128010', 'Tehran'),
    ('Salar', 'Sharifi', 'dr', 1, 5, '09920615020', 'Tehran'),
    ('Hamed', 'Azizi', 'master', 0, 6, '09112223333', 'Isfahan'),
    ('Amir', 'Adibi', 'master', 1, 4, '09123456789', 'Shiraz'),
    ('Reza', 'Mohammadi', 'dr', 0, 3, '09111111111', 'Mashhad'),
    ('Farshid', 'Sameri', 'master', 0, 4, '09987654321', 'Tehran'),
    ('Ehsan', 'Naseri', 'dr', 1, 2, '09222222222', 'Isfahan'),
]

cursor.executemany(SQL, values)


# -------------------- insert to students table --------------------
SQL = """
INSERT INTO students(
    name,
    family,
    field_ID,
    entering_year,
    address,
    average
)
VALUES(%s, %s, %s, %s, %s, %s)
"""

values = [
    ('Mohammad', 'Dori', 1, 1400, 'Tehran', 20),
    ('Ali', 'Mohammad', 1, 1390, 'Tehran', 19),
    ('Ali', 'Adibi', 4, 1395, 'Isfahan', 10),
    ('Salar', 'Sharifi', 5, 1401, 'Isfahan', 5),
    ('Mohammad', 'Azizi', 2, 1399, 'Shiraz', 18.75),
    ('Sara', 'Nasiri', 3, 1398, 'Tabriz', 13),
    ('Nazanin', 'Dori', 3, 1400, 'Mashhad', 12.88),
    ('Amir', 'Amiri', 6, 1395, 'Guilan', 19.93),
    ('Reza', 'Talebi', 6, 1395, 'Yazd', 11),
    ('Reza', 'Dori', 6, 1389, 'Qum', 10.5),
    ('Mohammad', 'Dori', 5, 1397, 'Isfahan', 14.2),
]

cursor.executemany(SQL, values)


# for save changes in database
database_connection.commit()
