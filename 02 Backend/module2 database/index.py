from flask import Flask
from flask import render_template
from flask import request
from DB_Connect import *

app = Flask('orbital')

#check against database for login info
def is_valid_login(username,passowrd):
	return True

def log_the_user_in(username):
	return 'logged in as {}'.format(username)

#index page
@app.route('/')
def index():
	return render_template('index.html')

#login page
@app.route('/login', methods=['POST', 'GET'])
def login():
	error = None
	if request.method == 'POST':
		if is_valid_login(request.form['username'],request.form['password']):
			return log_the_user_in(request.form['username'])
		else:
			error = 'Invalid username/password'
    	return render_template('login.html',error = error)

#registry page
@app.route('/registry', methods = ['POST', 'GET'])
def register():
        error = None
        if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']
                if add_user(username,password):
                        return 'Welcome, {}'.format(username)
                else:
                        error = 'Repeated Username'
        return render_template('user_registration.html', error = error)

app.run()
