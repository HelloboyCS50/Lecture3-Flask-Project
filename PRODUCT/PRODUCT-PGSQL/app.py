from flask import Flask , render_template , request , url_for , redirect

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session , sessionmaker


app = Flask(__name__)

engine = create_engine("postgresql://postgres:1234@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind = engine))


# class Product():

# 	id = db.Column(db.Integer , primary_key =True)
# 	text = db.Column(db.String(200))
# 	complete = db.Column(db.Boolean)


@app.route('/')
def index():
	return render_template('index.html')

# To show input item

# @app.route('/add' , methods = ['POST'])
# def add():
# 	productname = request.form.get('productname')
# 	return f' Your Inputed item is : {productname}'

# To connect Data in the Database

# @app.route('/add' , methods = ['POST'])
# def add():
# 	product = Product(text=request.form['productname'] , complete = False)
	# db.session.add(product)
	# db.session.commit()
	# return redirect(url_for('index'))

# Write for pgsql

@app.route('/add' , methods = ['POST'])
def add():
	# product = Product(text=request.form['productname'] , complete = False)
	product = db.execute('SELECT * FROM product').fetchall()
	db.add(product)
	db.commit()
	return redirect(url_for('index'))




if __name__ == '__main__':
	app.run(debug=True)














