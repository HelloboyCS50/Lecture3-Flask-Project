import os

from flask import Flask , render_template , request ,redirect , session

# from sqlalchemy import create_engine

# from sqlalchemy.orm import scoped_session  , sessionmaker

import mysql.connector

app = Flask(__name__)

app.secret_key = os.urandom(24)

# engine = create_engine("postgresql://postgres:1234@localhost:5432/postgres")

# db = scoped_session(sessionmaker(bind = engine))


# For show data in MYSal

conn =mysql.connector.connect(host='localhost',
                              database='login',
                              user=' root',
                              password='')

cursor=conn.cursor()


@app.route('/') 
def login():
	return render_template('login.html')


@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/dashboard')
def dashboard():
	if 'user_id' in session:
		return render_template('dashboard.html')
	else:
		return redirect('/')


@app.route('/login_validation' , methods = ['POST'])
def login_validation():

	email = request.form.get('email')
	password = request.form.get('password')

	# users = db.execute('SELECT * FROM users WHERE email=:email AND password=:password' ,
	# 	{'email' : email , 'password' : password}).fetchall()

	# Mysql

	cursor.execute('SELECT * FROM users WHERE email LIKE %s AND password LIKE %s',
		(email,password))

	users = cursor.fetchall()


	if len(users)>0:

		session['user_id'] = users[0][0] # Add new key by name of user id this will be = to user which is 
										# my list first item or my tuple first item.

		# return render_template('home.html')
		return redirect('/dashboard') # Use home function

	else:
		# return render_template('login.html')
		return redirect('/') # Use index or login function


@app.route('/add_user' , methods = ['POST'])
def add_user():

	name = request.form.get('name')
	email = request.form.get('email')
	password = request.form.get('password')

	
	# db.execute('INSERT INTO users (name , email , password) VALUES ( :name , :email , :password)' ,
	# 	{'name' : name , 'email' : email , 'password' : password})


	# Mysql

	cursor.execute('INSERT INTO `users` VALUES (NULL , %s , %s , %s) ' ,
		(name , email , password))


	conn.commit() # To save this in database table


	# Directly go after registation in Postsql

	# users = db.execute('SELECT * FROM users WHERE email=:email AND password=:password' ,
	# 	{'email' : email , 'password' : password}).fetchall()
	# session['user_id'] = users[0][0]


	# Directly go after registation in mysql

	cursor.execute('SELECT * FROM users WHERE email LIKE %s AND password LIKE %s',
		(email,password))

	users = cursor.fetchall()

	session['user_id'] = users[0][0]


	return redirect('/dashboard')






@app.route('/logout')
def logout():
	session.pop('user_id') # To make log out everywhere
	return redirect('/')

if __name__=='__main__':
	app.run(debug=True)