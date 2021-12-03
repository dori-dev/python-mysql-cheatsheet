"""Select data from two table
"""
from mysql import connector


def show_sql_result(sql: str):
    cursor.execute(sql)

    result = cursor.fetchall()

    for record in result:
        print(record)


database_connection = connector.connect(
    host="localhost",
    user="user",
    passwd="password",
    database="py_university"
)

cursor = database_connection.cursor()


# Extract the list of software students
print("------------------------- 6 -------------------------")
SQL = """
SELECT student_ID, student_name, student_family
FROM students, field
WHERE students.field_ID = field.field_ID and orientation='software'
"""
show_sql_result(SQL)

# Extract the list of computer school courses
print("------------------------- 7 -------------------------")
SQL = """
SELECT field_ID, orientation, course
FROM field, faculty
WHERE field.faculty_ID = faculty.faculty_ID and faculty_name='computer faculty'
"""
show_sql_result(SQL)
