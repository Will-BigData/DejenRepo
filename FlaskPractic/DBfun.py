import sqlite3
import pandas as pd

conn=sqlite3.connect('students.db')

c=conn.cursor()

c.execute("""CREATE TABLE students (name TEXT, age INTEGER)""")

c.execute("""INSERT INTO students VALUES ('Mark',17)""")

c.execute("""SELECT * FROM students""")

rows = c.fetchall()

for row in rows:
    print(row)

conn.commit()
