import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative

base = sqlalchemy.ext.declarative.declarative_base()

class student(base):
	__tablename__ = 'student'
	id = sqlalchemy.Column(sqlalchemy.Integer,primary_key = True)
	username = sqlalchemy.Column(sqlalchemy.String(15))
	password = sqlalchemy.Column(sqlalchemy.String(20))
	timetable = sqlalchemy.Column(sqlalchemy.TEXT(672))

def create_session():
	engine = sqlalchemy.create_engine('mysql+pymysql://root:88964415@45.63.84.203:3306/orbital')
	db_session = sqlalchemy.orm.sessionmaker(bind = engine)
	return db_session()

def non_exist(username,session):
	query = session.query(student).filter(student.username == username)
	if not query.first():
		return True
	else:
		return False
def add_user(username,password):
	session = create_session()
	if non_exist(username,session):
		new_user = student(username = username,password = password)
		session.add(new_user)
		session.commit()
		session.close()
	else:
		return False