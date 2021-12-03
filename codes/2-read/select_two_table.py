"""select data from two table with where(conditions)
first see `select_where.py`!
"""
from mysql import connector


def show_sql_result(sql: str):
    """show result of sql script

    Args:
        sql (str): sql script
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    for record in result:
        print(record)


database_connection = connector.connect(
    host="localhost",
    user="user",
    passwd="password",
    database="university"
)

cursor = database_connection.cursor()


# Extract the list of software students
print("------------------------- 6 -------------------------")
SQL = """
SELECT student_ID, name, family
FROM students, field
WHERE students.field_ID = field.field_ID and orientation='software'
"""
show_sql_result(SQL)

# Extract the list of computer faculty courses
print("------------------------- 7 -------------------------")
SQL = """
SELECT field_ID, orientation, grade
FROM field, faculty
WHERE field.faculty_ID = faculty.faculty_ID and faculty.name='computer'
"""
show_sql_result(SQL)
