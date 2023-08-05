import sqlite3
from datetime import date

conn = sqlite3.connect('db2.sqlite')

cursor = conn.cursor()

cursor.execute("CREATE TABLE Students (id int, name Varchar(32), surname Varchar(32), city Varchar(32))")

cursor.executemany("INSERT INTO Students VALUES (?,?,?,?)", [( 'Max', 'Brooks', '24', 'Spb'),( 'John', 'Stones', '15', 'Spb'), ( 'Andy', 'Wings', '45', 'Manhester'), ('Kate', 'Brooks', 34, 'Spb')])

cursor.execute("SELECT FROM Students")

print(cursor.fetchall())
#conn.commit()
#conn.close()


#cursor.execute("CREATE TABLE Courses (id int, name Varchar(32), time_start timestamp, time_end timestamp)")

#cursor.execute("CREATE TABLE Student_courses (student_id int, course_id int)")

conn.commit()

cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)", [('1', 'python', "21.07.21", "21.08.21"),('2', 'java', "13.07.21", "16.08.21")])

cursor.executemany("INSERT INTO Student_courses VALUES (?,?)", [(1,1), (2,1), (3,1), (4,2)])
conn.commit()
conn.close()