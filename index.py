from flask import Flask
from flask import render_template
from flask import request

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

app.run()
