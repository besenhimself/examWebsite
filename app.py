from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        return redirect(url_for('success', name = user))
    else:
        return render_template('login.html')

@app.route('/home/<name>')
def success(name):
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug = True)