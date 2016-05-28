import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative

base = sqlalchemy.ext.declarative.declarative_base()

class student(base):
	__tablename__ = 'student'
	id = sqlalchemy.Column(sqlalchemy.Integer,primary_key = True)
	username = sqlalchemy.Column(sqlalchemy.String(8))
	password = sqlalchemy.Column(sqlalchemy.String(32))

engine = sqlalchemy.create_engine('mysql+pymysql://root:88964415@127.0.0.1:3306/Orbital')
db_session = sqlalchemy.orm.sessionmaker(bind = engine)

session = db_session()
new_user = student(username = 'A0131282',password = 'B7a8281828?')

session.add(new_user)
session.commit()
session.close()
