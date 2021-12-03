"""select data from table with where(conditions)
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

# Extract the list of all students in Tehran.
print("------------------------- 1 -------------------------")
SQL = "SELECT name, family FROM students WHERE address='tehran'"
show_sql_result(SQL)


# Extract the list of university professors who are faculty members.
print("------------------------- 2 -------------------------")

SQL = "SELECT * FROM professors WHERE faculty_member='1'"
show_sql_result(SQL)

# Extract the list of conditional students.
print("------------------------- 3 -------------------------")
SQL = "SELECT * FROM students WHERE average<12"
show_sql_result(SQL)

# Extract the list of students with a grade point average above 17 in order of grade point average.
print("------------------------- 4 -------------------------")
# You can use `DESC` Descending sort or `ASC` Ascending sort
SQL = "SELECT * FROM students WHERE average>=17 order by average DESC"
show_sql_result(SQL)


# Extract the list of professors with doctoral degrees
print("------------------------- 5 -------------------------")
SQL = "SELECT * FROM professors WHERE degree='dr'"
show_sql_result(SQL)
