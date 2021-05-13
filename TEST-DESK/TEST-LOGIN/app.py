from flask import Flask , render_template , request , session ,redirect
import mysql.connector
import os

app = Flask(__name__)

app.secret_key = os.urandom(20)

conn = mysql.connector.connect(host = 'localhost' , database = 'webdesk' , user = 'root' ,
	password = '')

cursor = conn.cursor()


@app.route('/')
def login():
	return render_template('login.html')


@app.route('/register')

def register():
	return render_template('register.html')


@app.route('/home')
def home():
	if 'user_id' in session:

		return render_template('home.html')

	else:

		# return render_template('login.html')
		return redirect('/')


# Dynamic

@app.route('/login_valid' , methods = ['POST'])
def login_valid():
	if request.method == 'POST':
		
		email = request.form.get('email')
		password = request.form.get('password')

		cursor.execute('SELECT * FROM appuser WHERE email LIKE %s AND password LIKE %s' ,(email , password))

		myuser = cursor.fetchall()

		if len(myuser) > 0 :
			session['user_id'] = myuser[0][0]

			return redirect('/home')

		else:

			return redirect('/register')



@app.route('/add_user' , methods = ['POST'])
def add_user():
	if request.method == 'POST':

		name = request.form.get('name')
		email = request.form.get('email')
		password = request.form.get('password')


		cursor.execute('INSERT INTO `appuser` VALUES (NULL , %s , %s , %s) ' , (name , email , password))
		conn.commit()

		cursor.execute('SELECT * FROM appuser WHERE email LIKE %s AND password LIKE %s' ,(email , password))

		myuser = cursor.fetchall()

		session['user_id'] = myuser[0][0]


		return render_template('home.html')

@app.route('/logout')
def logout():
	session.pop('user_id')# To make log out everywhere
	return redirect('/')

if __name__ == '__main__':
	app.run(debug= True)