import os
from flask import Flask , render_template , request , url_for , session ,redirect

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session , sessionmaker

engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres')
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

app.secret_key = os.urandom(34)

@app.route('/')
def login():
	return render_template('login.html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/home')
def home():
	if 'user_id' in session: # To make access only register user

		return render_template('home.html')

	else:
		return redirect('/')


@app.route('/login_validation' , methods = ['POST'])
def login_validation():
	email = request.form.get('email')
	password = request.form.get('password')

	# This is mysql query 

	# cursor.execute('SELECT * FROM user WHERE email LIKE %s AND password LIKE %s ' ,(email , password))

	# user = cursor.fetchall()

	# This is postgres query

	user = db.execute('SELECT * FROM users WHERE email=:email AND password=:password' ,
		{'email' : email , 'password' : password}).fetchall()

	if len(user) > 0:
		session['user_id'] = user[0][0]
		# return render_template('home.html')
		return redirect('/home')

	else:
		# return render_template('register.html')
		return redirect('/register')


@app.route('/add_user' , methods = ['POST'])
def add_user():
	name = request.form.get('name')
	email = request.form.get('email')
	password = request.form.get('password')

	# This is mysql query 

	# cursor.execute('INSERT INTO `user` VALUES (NULL , %s , %s , %s) ' , (name , email , password))

	# This is postgres query

	db.execute('INSERT INTO users (name , email , password) VALUES ( :name , :email , :password) ' , 
		{'name' : name , 'email' : email , 'password' : password}) 

	# Insert item not use fatchall()

	db.commit()

	# TO directly show home page a user when he fill the registation form


	new_user = db.execute('SELECT * FROM users WHERE email=:email AND password=:password' ,
		{'email' : email , 'password' : password}).fetchall()

	session['user_id'] = new_user[0][0]

	return redirect('/home')




@app.route('/logout')
def logout():
	session.pop('user_id') # Use python pop to delete user id
	return redirect('/')




















if __name__ == '__main__':

	app.run(debug=True)