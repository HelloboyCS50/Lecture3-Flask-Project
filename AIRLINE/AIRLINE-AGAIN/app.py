from flask import Flask , render_template , request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session , sessionmaker

engine = create_engine("postgresql://postgres:1234@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind = engine))




app = Flask(__name__)



@app.route('/')
def index():
	flights = db.execute('SELECT * FROM flights').fetchall()

	return render_template('index.html' , flights = flights)






# Make Dynamic


@app.route('/book' , methods = ['POST'])
def book():

	name = request.form.get('name')
	try:
		flight_id = int(request.form.get('flight_id'))

	except ValueError:
		return render_template('error.html', message = 'Invaid Flight Number !')

		# If the person give valid flight number...

	if db.execute('SELECT * FROM flights WHERE id = id' , {'id' : flight_id}).rowcount == 0:

		return render_template('error.html' , message = 'There are No Flight !')

	else:
		db.execute('INSERT INTO passengers (name , flight_id) VALUES (:name , :flight_id)',
			{"name" : name , "flight_id" : flight_id})

	db.commit()


	return 'Your flight Successfully Store'









@app.route('/flights')

def flights():

	'''List All flights'''

	flights = db.execute('SELECT * FROM flights').fetchall()
	return render_template('flight_list.html', flights = flights)


@app.route('/flights/<int:flight_id>')

def flight(flight_id):

	flight = db.execute('SELECT * FROM flights WHERE id = :id ' , {'id' : flight_id}).fetchone()

	if flight is None:

		return render_template('error.html' , message = 'No such Flight here..!')

	# Get all passengers

	else:

		passengers = db.execute('SELECT name FROM passengers WHERE flight_id = :flight_id' , {'flight_id' : flight_id}).fetchall()
		return render_template('flight_details.html' , flight = flight , passengers = passengers )








if __name__=='__main__':
	app.run(debug=True)


