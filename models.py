from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """
    The basic user model which can be used as an object either created by the server (when a user first registers) or
    when the respective user is retrieved from the sqlite database.
    
    @Attributes
    id [INT] - The unique identification number assigned to all users upon entry to the database.
    email [STR] - The user's email address, must also be unique
    password [STR] - The user's password, will be the hashed password in future versions
    prefname [STR] - The name the user prefers to be called, such as Elina or Ziggy
    dob [DATETIME.DATE] - The user's date of birth to help pair peers
    gender [STR] - The user's gender, again to aid in the selection of a partner
    preferredGym [STR] - The user's gym, matching will only look for users who attend the same gym
    """

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

    #The following 4 methods are required by flask-login
    def is_active(self):
        #Always true as there are no non-logged users, returns whether the user is an active account or not
        return True
    
    def get_id(self):
        #Return the user's ID
        return self.id
    
    def is_authenticated(self):
        #Always true as there are no non-logged users
        return True
    
    def is_anonymous(self):
        #Always false as there are no non-logged users
        return False

    @staticmethod
    def findUserByEmail(em):
        # Retrieves a user object from the database given an email address
        print(em)
        return User.query.filter(User.email == em).first()
    
    @staticmethod
    def findUserByID(id):
        # Retrieves a user object from the database given a user ID
        return User.query.filter(User.id == id).first()
    
    @staticmethod
    def passwordIsMatch(em, pw):
        # Verifies that the password of the user corresponding to the provided email matches the one stored in the database
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
        # Matching algorithm for exercise routines, will be rewritten for Levenshtein Distance
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
    """
    Simple table to store the gym locations the application currently supports.

    @Attributes
    id [INT] - Unique identification number, created by database
    name [STR] - Gym name
    address [STR] - Address of gym, must be unique to help identify specific locations
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, unique=True)

    def __init__(self, name, address):
        self.name = name
        self.address = address

class Exercise(db.Model):
    """
    Simple table to store all exercises available for selection by users.

    @Attributes
    id [INT] - Unique identification number, created by database
    name [STR] - Name of exercise, must be unique
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    def __init__(self, name):
        self.name = name