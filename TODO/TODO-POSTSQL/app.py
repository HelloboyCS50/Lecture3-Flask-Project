from flask import Flask , render_template , request 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session , sessionmaker


app = Flask(__name__)

engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres')
db = scoped_session(sessionmaker(bind=engine))



@app.route('/')
def index():
	return render_template('index.html')



@app.route('/submit_form' , methods = ['POST'])
def form_submit():
	if request.method == 'POST':
		task = request.form['task']
		
		# Write query

		# cursor.execute('INSERT INTO `tasks` ( id ,title) VALUES (NULL , %s)' , (task))

		db.execute('INSERT INTO tasks (title) VALUES (:task)' ,
			{'task' : task})

		db.commit()


		return f'Your task {task}'



if __name__=='__main__':
	app.run(debug=True)










