
from peewee import *

conn = SqliteDatabase('db1.sqlite')

class Student(Model):

    id = IntegerField(column_name = 'id', primary_key=True)
    name = CharField(column_name = 'name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name = 'age')
    cuty = CharField(column_name='city')

    class Meta:
        database = conn

class Courses(Model):

    id = IntegerField(column_name = 'id', primary_key=True)
    name = CharField(column_name = 'name')
    time_start = DateTimeField(column_name = 'tinme_start')
    time_end = DateTimeField(column_name = 'time_end')

    class Meta:
        database = conn

class Student_courses(Model):
    student_id = ForeignKeyField(Student)
    course_id = ForeignKeyField(Courses)

    class Meta:
        database = conn
#Student.create_table()
#Student_courses.create_table()
#Courses.create_table()
student = Student(name="Max", surname="Brooks", age=24, city="Spb")
student.save()
student = Student(name="John", surname="Stones", age=15, city="Spb")
student.save()
student = Student(name="Andy", surname="Wings", age=45, city="Manchester")
student.save()
student = Student(name="Kate", surname="Brooks", age=34, city="Spb")
student.save()

courses = Courses(name="python", time_start="21.07.2021", time_end="21.08.2021")
courses.save()
courses = Courses(name="java", time_start="13.07.2021", time_end="16.08.2021")
courses.save()

student_course = Student_courses(student_id=1, courses_id=1)
student_course.save()
student_course = Student_courses(student_id=2, courses_id=1)
student_course.save()
student_course = Student_courses(student_id=3, courses_id=1)
student_course.save()
student_course = Student_courses(student_id=4, courses_id=2)
student_course.save()

student_30 = Student.select().where(Student.age > 30)
for i in student_30:
    	print(i.name)

students_python = Student.select().join(Student_courser).where(Student_courser.course_id == 1)
for r in students_python:
	print(r.name, r.surname)


students_spb = Students.select().join(Student_courser).where(
    Student_courser.course_id == 1, Students.city == 'Spb')
for k in students_spb:
    print(k.name, k.surname)
