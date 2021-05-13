from flask import Flask  , render_template , request , redirect , url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)




app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'# when database file location with app.py


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db' #relative path

db = SQLAlchemy(app)

class Todo(db.Model):

	id = db.Column(db.Integer , primary_key = True)
	text = db.Column(db.String(200))
	complete = db.Column(db.Boolean)


@app.route('/')
def index():
	# todos = Todo.query.all() # To load all item in index.html from database
	incomplete = Todo.query.filter_by(complete = False).all() # To see all incomplete items.
	complete = Todo.query.filter_by(complete = True).all()
	return render_template('index.html', incomplete = incomplete , complete = complete)#see complete


@app.route('/add' , methods = ['POST'])
def add():

	todo = Todo(text=request.form['todoitems'] , complete=False)
	db.session.add(todo)
	db.session.commit()
	return redirect(url_for('index'))


@app.route('/complete/<id>')
def complete(id):

	todo = Todo.query.filter_by(id=int(id)).first() # To query all item from data base
	todo.complete = True
	db.session.commit()

	return redirect(url_for('index')) # To stay in index.html files



# Try another way (28 to 30 line)

# @app.route('/add' , methods=['POST'])
# def add():
# 	todoitems = request.form.get('todoitems')
# 	return f'<h1> Your input Item is : {todoitems} </h1>'











if __name__=='__main__':
	app.run(debug=True)