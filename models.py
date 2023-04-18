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
        
    """ def routine_match(self, user_pool):
        print('User pool:', user_pool)
        currentuser_set = user_pool[self.id]
        routinematchdictionary = {}
        final_dictionary = {}

        for i in range(len(user_pool)):

            if user_pool[i] == self:

                continue

            partneruser_set = user_pool[i].routineset
            print ('partner set', partneruser_set)
            overlap_set = currentuser_set.intersection(partneruser_set)
            length_overlap = len(overlap_set)
            routinematchdictionary[user_pool[i]] = length_overlap

        sorted_routinematchdictionary = sorted(routinematchdictionary.items(),
        key = lambda x:x[1], reverse = True)

        final_dictionary = dict(sorted_routinematchdictionary)

        return final_dictionary """
    
    def routine_match(self, user_pool):
        print('User pool:', user_pool)
        currentuser_set = user_pool[self.id]
        routinematchdict = {}
        final_dictionary = {}

        for id in user_pool:
            if id == self.id:
                continue

            partneruser_set = user_pool[id]
            print('partner set: ', partneruser_set)
            overlap_set = currentuser_set.intersection(partneruser_set)
            length_overlap = len(overlap_set)
            routinematchdict[id] = length_overlap

        sorted_routinematchdictionary = sorted(routinematchdict.items(),
        key = lambda x:x[1], reverse = True)

        print(sorted_routinematchdictionary)

        return sorted_routinematchdictionary


class Gym(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, unique=True)

    def __init__(self, name, address):
        self.name = name
        self.address = address

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    def __init__(self, name):
        self.name = name