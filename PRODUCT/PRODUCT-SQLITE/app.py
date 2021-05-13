from flask import Flask , render_template , request , url_for , redirect

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'

db = SQLAlchemy(app)

class Product(db.Model):

	id = db.Column(db.Integer , primary_key =True)
	text = db.Column(db.String(200))
	complete = db.Column(db.Boolean)


@app.route('/')
def index():
	return render_template('index.html')

# To show input item

# @app.route('/add' , methods = ['POST'])
# def add():
# 	productname = request.form.get('productname')
# 	return f' Your Inputed item is : {productname}'

# To connect Data in the Database

@app.route('/add' , methods = ['POST'])
def add():
	product = Product(text=request.form['productname'] , complete = False)
	db.session.add(product)
	db.session.commit()
	return redirect(url_for('index'))







if __name__ == '__main__':
	app.run(debug=True)












