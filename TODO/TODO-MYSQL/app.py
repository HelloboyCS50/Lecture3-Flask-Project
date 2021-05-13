from flask import Flask , render_template , request 

import mysql.connector
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)


conn = mysql.connector.connect(host='localhost',
                              database='to_do',
                              user='root',
                              password='')

cursor= conn.cursor()

@app.route('/')
def index():
	return render_template('index.html')



@app.route('/submit_form' , methods = ['POST'])
def form_submit():
	if request.method == 'POST':
		task = request.form.get('task')
		

		# cursor.execute("INSERT INTO `tasks` VALUES (NULL , %s)" , (task))

		# cursor.execute('INSERT INTO `tasks` (`id`, `title`, `created_at`) VALUES (NULL, %s, current_timestamp())')
		cursor.execute('INSERT INTO `tasks` VALUES (NULL, %s, current_timestamp()) ' , (task))

		conn.commit()

		return 'Success !'

		



if __name__=='__main__':
	app.run(debug=True)











