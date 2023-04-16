# GROUP: Gym Buddy
# MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
# COURSE: CMSC 495:7383
# FILE: gymBuddy.py
# DATE: April 9, 2023

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login.login_manager import LoginManager
from flask_login import current_user
from models import User, Exercise, db

SECRET = "dasibasdbhjalfhjblahjksdfb"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gymbuddy.db"
app.config["SECRET_KEY"] = SECRET
db.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)

from main_views import main_views
app.register_blueprint(main_views)
from auth import auth
app.register_blueprint(auth)



""" class User:
    id = 1
    username = 'brenden'
    password = 'test123'
    prefName = 'bc'
    dob = '5/5/5'
    gender = 'male' """

""" currentUser = User() """
""" 
def getUserID(user):
    return user.id

def getCurrentUser():
    return current_user """


@login_manager.user_loader
def load_user(user_id):
    # return User.get(user_id)
    return User.findUserByID(user_id)


""" @app.route('/', methods=["GET", "POST"])
@app.route('/login', methods=["GET", "POST"])
def loginPage():
    if request.method == "POST":
        usr = request.form.get('email')
        pwd = request.form.get('psw')

        if (usr == current_user.username and pwd == currentUser.password):
            id = getUserID(currentUser)
            return redirect(url_for('profilePage', userID = id))
        else:
            return render_template("html/login.html", error="Invalid Login")
    return render_template("html/login.html")


    # Below is for JSON data only.
    ##############################
    # jsonData = request.get_json()
    # usr = (jsonData['uname'])
    # pwd = (jsonData['psw'])
    # error = None
    # if request.method == 'POST':
    #     if request.form['username'] != 'admin' or request.form['password'] != 'admin':
    #         error = 'Invalid Credentials. Please try again.'
    #     else:
    #         return redirect(url_for('home'))
    # return render_template('login.html', error=error)




@app.route('/createAccount', methods=["GET", "POST"])
def createAccount():
    if request.method == "POST":
        msg = ""
        valid = True

        prefName = str(request.form.get('prefName'))
        email = str(request.form.get('email'))
        password1 = str(request.form.get('pwd1'))
        password2 = str(request.form.get('pwd2'))
        dob = str(request.form.get('dateOfBirth'))
        gender = str(request.form.get('gender'))
        prefGym = str(request.form.get('prefGym'))

        #Validation here?
        if not (len(password1) >= 8):
            valid = False
            msg = "Password invalid"
        
        if not (len(password2) >= 8):
            valid = False
            msg = "Password invalid"

        if not (password1 == password2):
            valid = False
            msg = "Passwords don't match"

        print(prefName)
        print(email)
        print(password1)
        print(password2)
        print(dob)
        print(gender)
        print(prefGym)

        if(valid):
            # Generate ID?
            # Input into DB?
            return redirect(url_for('welcomePage'))
        else:
            return render_template("html/createAccount.html", error = msg)

    return render_template("html/createAccount.html")



@app.route('/profilePage/<userID>')
def profilePage(userID):

    return render_template("html/profilePage.html", 
        profileHeader = currentUser.username + "'s",
        uName = currentUser.username, 
        prefName = currentUser.prefName, 
        dob = currentUser.dob, 
        gender = currentUser.gender)


@app.route('/findBuddy', methods=["GET", "POST"])
def findBuddy():
    cUser = current_user
    if request.method == "POST":
        exSquats = request.form.get('squats')
        exTriceps = request.form.get('triceps')
        if(exSquats):
            # MATCHING OCCURS HERE?
            return redirect(url_for('welcomePage'))
        
    return render_template("html/findBuddy.html", id = getUserID(currentUser))


@app.route('/welcomePage')
def welcomePage():
    return render_template("html/welcomePage.html") """

if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=True, port=5000)
