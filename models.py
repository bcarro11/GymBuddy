from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    prefname = db.Column(db.String, nullable=False)
    dob = db.Column(db.Date)
    gender = db.Column(db.String)
    preferredGym = db.Column(db.Integer)

    def __init__(self, email, password, prefname, dob, gender, preferredGym):
        self.email = email
        self.password = password
        self.prefname = prefname
        self.dob = dob
        self.gender = gender
        self. preferredGym = preferredGym

    def is_active(self):
        return True
    
    def get_id(self):
        return self.id
    
    def is_authenticated(self):
        return True
    
    def is_anonymous(self):
        return False

    @staticmethod
    def findUserByEmail(em):
        # return db.session.execute(db.select(User).filter_by(email=em)).scalar_one()
        print(em)
        return User.query.filter(User.email == em).first()
    
    @staticmethod
    def findUserByID(id):
        #return db.session.execute(db.select(User).filter_by(id=id)).scalar_one()
        return User.query.filter(User.id == id).first()
    
    @staticmethod
    def passwordIsMatch(em, pw):
        user = User.findUserByEmail(em)
        if user and pw == user.password:
            return user
        else:
            return None


class Gym(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, unique=True)

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)