from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, user_logged_in, user_unauthorized, login_user
from datetime import date
from models import db, User

main_views = Blueprint('main_views', __name__)

@main_views.route('/', methods=["GET", "POST"])
@main_views.route('/login', methods=["GET", "POST"])
def loginPage():
    if request.method == "POST":
        usr = request.form.get('email')
        pwd = request.form.get('psw')

        user = User.passwordIsMatch(usr, pwd)
        if user:
            login_user(user)
            return redirect(url_for('main_views.profilePage', userID = user.id))
        else:
            return render_template("html/login.html", error="Invalid Login")
    return render_template("html/login.html")

@main_views.route('/createAccount', methods=["GET", "POST"])
def createAccount():
    if request.method == "POST":
        msg = ""
        valid = True

        prefName = str(request.form.get('prefName'))
        email = str(request.form.get('email'))
        password1 = str(request.form.get('pwd1'))
        password2 = str(request.form.get('pwd2'))
        dobstr = str(request.form.get('dateOfBirth'))
        print(dobstr)
        month = int(dobstr[5:7])
        day = int(dobstr[8:])
        year = int(dobstr[:4])
        dob = date(year, month, day)
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

        if "@" not in email:
            valid = False
            msg = "Invalid email address"

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
            user = User(email=email, password=password1, dob=dob, gender=gender, preferredGym=prefGym, prefname=prefName)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main_views.welcomePage'))
        else:
            return render_template("html/createAccount.html", error = msg)

    return render_template("html/createAccount.html")

@main_views.route('/profilePage/<userID>',  methods=["GET", "POST"])
def profilePage(userID):
    user = db.get_or_404(User, userID)
    
    #Check if it's user's own profile page or if they have rated the other user before.
    myProfilePage = False
    alreadyRated = False

    #Get Rating
    getRating = 3

    #Submit user rating
    if request.method == "POST":
        #Get Rating that was given by user
        rateUser = request.form['rateUser']
        
        #Add rating to DB here?
        print(rateUser)

        #Toggle Already Rated
        alreadyRated = True

    return render_template("html/profilePage.html", 
        profileHeader = user.prefname,
        uName = user.prefname, 
        prefName = user.prefname, 
        dob = str(user.dob), 
        gender = user.gender,
        prefGym = user.preferredGym,
        myPage = myProfilePage,
        rated = alreadyRated,
        rating = getRating)

@main_views.route('/welcomePage')
def welcomePage():
    return render_template("html/welcomePage.html")