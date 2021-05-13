import os
from flask import Flask , render_template , request

from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session , sessionmaker

app = Flask(__name__)


engine = create_engine("postgresql://postgres:1234@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind = engine))




@app.route('/')
def index():
	school = db.execute('SELECT * FROM school').fetchall()
	return render_template('index.html' , school = school)


@app.route('/addmission' ,methods = ['POST'])
def addmission():

	'''Addmission Now !'''

	# Get from information

	name = request.form.get('name')
	try:
		student_id = int(request.form.get('student_id'))

	except ValueError:
		return render_template('error.html', message = 'Invaid Student ID Number !')




	# Make sure it exiest


	if db.execute('SELECT * FROM school WHERE id = :id' , {'id' : student_id}).rowcount == 0:
		return render_template('error.html' , 'There are No Student here!')

	else:
		db.execute('INSERT INTO student_data (student_name , student_id) VALUES (:student_name , :student_id)',
			{'student_name' : name , 'student_id' : student_id})

	db.commit()
	return render_template('success.html')



@app.route('/school_list')
def school_list():

	'''List all school here'''

	school = db.execute('SELECT * FROM school').fetchall()
	return render_template('school_list.html' , school = school)

#List all details about single school

@app.route('/school_details/<int:school_id>')
def school_details(school_id):


	school_list = db.execute('SELECT * FROM school WHERE id = :id' , {'id' : school_id}).fetchone()

	if school_list is None:
		return render_template('error.html' , message = 'No such School Here')

	else:

		# Get All student

		student_data = db.execute('SELECT student_name FROM student_data WHERE student_id = :student_id' , {'student_id' : student_id}).fetchall()
		return render_template('school_details.html' , school_list = school_list , student_data = student_data)


































