from flask import Flask, render_template, url_for, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length, InputRequired
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(16), unique = True)
    password = db.Column(db.String(80))

class Login(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min = 3, max = 16)])
    password = PasswordField('password', validators=[InputRequired(), Length(min = 4, max = 80)])

@app.route('/')
def index():
    return redirect('login')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    form = Login()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            if check_password_hash(user.password, from.password.data):
                return redirect(url_for('success', name = form.username.data))

    return render_template('login.html', form = form)

@app.route('/home/<name>')
def success(name):
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug = True)