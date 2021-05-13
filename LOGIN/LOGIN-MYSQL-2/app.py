from flask import Flask , render_template , request , session , redirect
import mysql.connector
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)


conn = mysql.connector.connect(host='localhost',
                              database='login',
                              user=' root',
                              password='')

cursor= conn.cursor()



@app.route('/')
def index():
	return render_template('login.html')



@app.route('/register')
def register():
	return render_template('register.html')


@app.route('/home')
def home():
	return render_template('home.html')


@app.route('/login_validation' , methods = ['POST'])
def login_validations():

	email = request.form.get('email') 
	password = request.form.get('password')

	cursor.execute('SELECT * FROM user WHERE email LIKE %s AND password LIKE %s' , (email,password))


	# Contain this query in the user variable

	user = cursor.fetchall()
	
	if len(user) > 0: # This means user are exist

		session['user_id'] = user[0][0]

		return render_template('home.html')
	else:
		return render_template('login.html')


@app.route('/add_user' , methods = ['POST'])
def add_user():
	name = request.form.get('name')
	email = request.form.get('email')
	password = request.form.get('password')

	cursor.execute('INSERT INTO `user` VALUES (NULL , %s , %s , %s) ' , (name, email , password))

	conn.commit() # Use commit to add item in the Databse

	cursor.execute('SELECT * FROM user WHERE email LIKE %s AND password LIKE %s' , (email , password))

	# Contain this query in myuser variable

	myuser = cursor.fetchall()

	session['user_id'] = myuser[0][0]

	return redirect('/home')

@app.route('/logout')
def logout():
	session.pop('user_id') # Use pop to delete item.
	return redirect('/')













if __name__=='__main__':
	app.run(debug=True)