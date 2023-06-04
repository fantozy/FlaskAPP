from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false



app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cvladi0 = db.Column(db.String(100))
    cvladi1 = db.Column(db.String(100))
    cvladi2 = db.Column(db.String(100))



@app.route('/')
def index():
    data = Data.query.all()
    return render_template('index.html', data=data )


@app.route('/insert', methods = ['POST'])
def insert():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    my_data = Data(cvladi0=name,cvladi1=email,cvladi2=phone)
    db.session.add(my_data)
    db.session.commit()
    flash("Product created")

    return redirect(url_for('index'))

@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
        my_data.cvladi0 = request.form['name']
        my_data.cvladi1 = request.form['email']
        my_data.cvladi2 = request.form['phone']

        db.session.commit()
        flash("Product updated")

        return redirect(url_for('index'))
    

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()

    flash("Product deleted")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
