import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative
from sqlalchemy.sql import exists, and_

base = sqlalchemy.ext.declarative.declarative_base()

class student(base):
	__tablename__ = 'student'
	id = sqlalchemy.Column(sqlalchemy.Integer,primary_key = True)
	username = sqlalchemy.Column(sqlalchemy.TEXT)
	password = sqlalchemy.Column(sqlalchemy.TEXT)
	token = sqlalchemy.Column(sqlalchemy.TEXT)
	timetable = sqlalchemy.Column(sqlalchemy.TEXT(672))

def create_session():
	#engine = sqlalchemy.create_engine('mysql+pymysql://root:88964415@45.63.84.203:3306/orbital')
	engine = sqlalchemy.create_engine('sqlite+pysqlite:///orbital.db')
	db_session = sqlalchemy.orm.sessionmaker(bind = engine)
	return db_session()

def is_exist(username,session):
	query = session.query(student).filter(student.username == username)
	if not query.first():
		return True
	else:
		return False

def add_user(username,password,token):
	session = create_session()
	if is_exist(username,session):
		new_user = student(username = username,password = password,token = token)
		session.add(new_user)
		session.commit()
		session.close()
		return True
	else:
		return False
		
def get_token(username):
	session = create_session()
	query = session.query(student).filter(student.username == username)
	if not query.first():
		return False
	else:
		return query.first().token

def auth(username,password):
	session = create_session()
	query = session.query(student).filter(and_(student.username == username,student.password == password))
	if not query.first():
		return False
	else:
		return True