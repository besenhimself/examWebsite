from flask import Flask, render_template, url_for, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length, InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class Login(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min = 3, max = 16)])
    password = PasswordField('password', validators=[InputRequired(), Length(min = 4, max = 24)])

@app.route('/')
def index():
    return redirect('login')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    form = Login()

    return render_template('login.html', form = form)
@app.route('/home/<name>')
def success(name):
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug = True)