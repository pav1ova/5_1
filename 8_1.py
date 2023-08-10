import sqlite3
from datetime import date

conn = sqlite3.connect('db1.sqlite')

cursor = conn.cursor()

#cursor.execute("CREATE TABLE Students (id int, name varchar(32), surname varchar(32), age int, city varchar(32))")
#cursor.execute("CREATE TABLE Courses (id int, name Varchar(32), time_start timestamp, time_end timestamp)")

#cursor.execute("CREATE TABLE Student_courses (student_id int, course_id int)")

cursor.execute('''INSERT INTO Students (id,name,surname, age, city) VALUES (1,'Max','Brooks',24 ,'Spb')''')
cursor.executemany('INSERT INTO Students VALUES(?,?,?,?,?)',[(2, 'John', 'Stones', 15, 'Spb'), (3, 'Andy', 'Wings', 45, 'Manhester'),(4, 'Kate','Brooks', 34, 'Spb')])


#conn.commit()
#conn.close()



#conn.commit()

cursor.executemany("INSERT INTO Courses (id, name, time_start, time_end) VALUES (?,?,?,?)", [(1, 'python', "21.07.21", "21.08.21"),(2, 'java', "13.07.21", "16.08.21")])

cursor.executemany("INSERT INTO Student_courses (student_id, course_id) VALUES (?,?)", [(1,1), (2,1), (3,1), (4,2)])
#conn.commit()
#conn.close()
more_30 = cursor.execute("SELECT name, age FROM Students WHERE age>30").fetchall()
study_python = cursor.execute('SELECT Students.name, Students.surname FROM Student_courses JOIN Students ON ''Student_courses.student_id = Students.id WHERE course_id = 1').fetchall()
study_python_from_spb= cursor.execute('SELECT Students.name, Students.surname FROM Student_courses JOIN Students ON ''Student_courses.student_id = Students.id WHERE course_id = 1 AND Students.city = "Spb"').fetchall()

print(more_30)
print(study_python)
print(study_python_from_spb)

conn.close()
