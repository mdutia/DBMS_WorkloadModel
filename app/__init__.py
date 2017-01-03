from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__, static_folder='static')
app.config.from_object('config')
db = SQLAlchemy(app)
Bootstrap(app)

from app import views

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False)

    def __init__(self ): 
        self.username=''

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<Admin %r>' % self.username


class WLM_data(db.Model):
    __tablename__='staff'
    id = db.Column(db.Integer, primary_key=True)    
    #Name
    title = db.Column(db.String(10))
    firstname= db.Column(db.String(40), unique=False)
    lastname= db.Column(db.String(40), unique=False)
    #centre= db.Column (db.String(120), unique=False)    
    #Staff/ student number
    position= db.Column (db.String(20), unique=False)
    total_hours= db.Column(db.Float)
    tot_research= db.Column (db.Float)
    tot_admin= db.Column (db.Float)
    tot_teaching= db.Column (db.Float)
    comment = db.Column(db.String(1024))
    research=  db.Column(db.String(2048))
    admin=  db.Column(db.String(2048))
    teaching=  db.Column(db.String(2048))

    def __init__(self, firstname='', lastname='', title='', position= '' ): 
        self.firstname, self.lastname, self.title, self.position = firstname, lastname, title, position
        self.total_hours= self.tot_admin= self.tot_research= self.tot_teaching = 0.0
        self.comment = ''
        self.research, self.teaching, self.admin= '','',''

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<Person %r>' % self.lastname

class AdminRole (db.Model):
    __tablename__='adminroles'
    id = db.Column(db.Integer, primary_key=True)
    #category= db.Column (db.String(10))  #Teaching, Research, Admin, Other
    description = db.Column(db.String(200))   
    tariff= db.Column(db.Float)
    multiplier= db.Column(db.Float)
    
    def __init__(self, description=' ', tariff= 0, multiplier= 1 ): 
        self.description, self.tariff, self.multiplier = description, tariff, multiplier
      
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return unicode(self.id) #'<User {0} {1}>'.format (self.id, self.firstname.encode('utf-8'), self.lastname) 

class ResearchRole (db.Model):
    __tablename__='research'
    id = db.Column(db.Integer, primary_key=True)
    #category= db.Column (db.String(10))  #Teaching, Research, Admin, Other
    description = db.Column(db.String(200))   
    tariff= db.Column(db.Float)
    multiplier= db.Column(db.Float)
    
    def __init__(self, description=' ', tariff= 0, multiplier= 1  ): 
        self.description, self.tariff, self.multiplier = description, tariff, multiplier
      
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return unicode(self.id) #'<User {0} {1}>'.format (self.id, self.firstname.encode('utf-8'), self.lastname) 

class TeachingRole (db.Model):
    __tablename__='teaching'
    id = db.Column(db.Integer, primary_key=True)
    #category= db.Column (db.String(10))  #Teaching, Research, Admin, Other
    description = db.Column(db.String(200))   
    tariff= db.Column(db.Float)
    multiplier= db.Column(db.Float)
    
    def __init__(self, description=' ', tariff= 0, multiplier= 1  ): 
        self.description, self.tariff, self.multiplier = description, tariff, multiplier
      
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return unicode(self.id) #'<User {0} {1}>'.format (self.id, self.firstname.encode('utf-8'), self.lastname) 


class Course(db.Model):
    __tablename__='courses'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(80), unique=True)
    category= db.Column(db.String(20), unique=False)
        
    def __init__(self, name= ' ', category=' ' ): 
        self.name= name
        self.category = category

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return '<Course: {0} {1}>'.format (self.id, self.name, self.category) 


login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return Admin.query.get(int(id))