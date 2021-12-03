"""create table in university database
"""

from mysql import connector

database_connection = connector.connect(
    host='localhost',
    user='salar',
    passwd='52212057',
    database='university'
)

cursor = database_connection.cursor()

# create `faculty` table
SQL = """
CREATE TABLE faculty(
    faculty_ID int not null,
    name varchar(40),
    admin varchar(20),
    fundation_year char(4),
    address varchar(100),
    primary key(faculty_ID)
)
"""
cursor.execute(SQL)

# create `field` table
SQL = """
CREATE TABLE field(
    field_ID int,
    field_name varchar(30),
    orientation varchar(50),
    grade varchar(30),
    faculty_ID int,
    primary key(field_ID),
    foreign key(faculty_ID) references faculty(faculty_ID)
)
"""
cursor.execute(SQL)

# create `students` table
SQL = """
CREATE TABLE students(
    student_ID int not null AUTO_INCREMENT,
    name varchar(20),
    family varchar(20),
    field_ID int not null,
    entering_year char(4),
    address varchar(100),
    average float,
    primary key(student_ID),
    foreign key(field_ID) references field(field_ID)
)
"""
cursor.execute(SQL)

# create `professors` table
SQL = """
CREATE TABLE professors(
    professor_ID int not null AUTO_INCREMENT,
    name varchar(20),
    family varchar(20),
    degree varchar(30),
    faculty_member bit,
    faculty_ID int,
    phone char(20),
    address varchar(100),
    primary key(professor_ID),
    foreign key(faculty_ID) references faculty(faculty_ID)   
)
"""
cursor.execute(SQL)

# show all tables
SQL = "SHOW TABLES"
cursor.execute(SQL)

for table in cursor:
    print(*table)
