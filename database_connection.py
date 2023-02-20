import sqlite3
connection = sqlite3.connect("company.db")

cursor = connection.cursor()

"""sql_command = 
CREATE TABLE employee ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE,
birth_date DATE);"""

sql_command = """
INSERT INTO employee (staff_number, fname, lname, gender, joining, birth_date) 
VALUES (NULL, "Skand", "Tiwari", "M", "2023-01-11", "2000-08-13");
"""

sql_view = """SELECT * FROM employee"""

staff_data = [ (2, "William", "Shakespeare", "m", "1961-10-25", "2023-01-11"),
               (3, "Frank", "Schiller", "m", "1955-08-17", "2023-01-11"),
               (4, "Jane", "Wall", "f", "1989-03-14", "2023-01-11") ]


"""for p in staff_data:
    format_str = 
INSERT INTO employee (staff_number, fname, lname, gender, joining, birth_date) 
VALUES ("{}", "{}", "{}", "{}", "{}", "{}");
"""
"""sql_command = format_str.format(p[0], p[1], p[2], p[3], p[4], p[5])
    cursor.execute(sql_command)"""


cursor.execute("""SELECT * FROM employee""")
print(cursor.fetchall())

connection.commit()
connection.close()

