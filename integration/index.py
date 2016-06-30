from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
import database.DB_Connect
import timetable.Timetable_Handler

app = Flask('orbital')
app.secret_key = "ThisIsASecretKeyThatYouShallNeverKnow"

@app.route('/homepage')
def homepage():
        username = session.get('username', None)
        if username:
            token = database.get_token(username)
            #return timetable.timetable_string(token)
            return render_template('/homepage/homepage.html')
        else:
            return render_template('/login/login.html', errormsg = "Please Login")

@app.route('/signup', methods = ['POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        token = session.get('token', None)
        if database.add_user(username, password, token):
            return render_template('/homepage/homepage.html')
        else:
            return "Error creating your account!"

@app.route('/receivetoken', methods = ['GET'])
def receivetoken():
    if request.method == 'GET':
        token = request.args.get('token', 0)
        session['token'] = token
        return render_template('/signup/signup.html')

#login page
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("/login/login.html")
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if database.auth(username, password):
            session['username'] = username
            return redirect(url_for('homepage'))
        else:
            errormsg = 'Invalid username/password'
            return render_template('/login/login.html', errormsg = errormsg)

app.run(host = "127.0.0.1", port = 5000, debug = True)
