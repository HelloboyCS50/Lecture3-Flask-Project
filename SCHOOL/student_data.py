
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session , sessionmaker

engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres')
db = scoped_session(sessionmaker(bind = engine))


def main():
	school = db.execute('SELECT id , name , location , student  FROM school').fetchall()

	for school_list in school:
		print(f'id {school_list.id} student_name : {school_list.name} Location : {school_list.location} Student : {school_list.student}')

	student_id = int(input('ID : '))

	school_list = db.execute('SELECT name , location , student FROM school WHERE id = :id' ,
		{'id' : student_id}).fetchone()


	if student_id is None:
		print('No student Here !')
		return

	else:
		student_data = db.execute('SELECT student_name FROM student_data WHERE student_id = :student_id' ,
			{'student_id' : student_id}).fetchall()


	print('Student : ')
	for student_student_name in student_data:
		print(student_student_name.student_name)

	if len(student_data) == 0:
		print('No Student here !')



if __name__ == '__main__':
	main()












