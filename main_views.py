from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, user_logged_in, user_unauthorized, login_user
from datetime import date
from models import db, User, Rating
from dotenv import load_dotenv
from os import getenv
from hashlib import sha256

#Load in enviornment variables held by .env
load_dotenv()
SALT = getenv("SALT")

main_views = Blueprint('main_views', __name__)

@main_views.route('/', methods=["GET", "POST"])
@main_views.route('/login', methods=["GET", "POST"])
def loginPage():
    """
    View for the login page which will allow the user to sign into their account. GET requests are handled as page requests
    while POST requests are handled as the user attempting to log in, verifying their identity first and then logging in
    through flask-login.
    """
    if request.method == "POST":
        usr = request.form.get('email')
        pwd = request.form.get('psw')
        hashedpwd = sha256((str(SALT) + pwd).encode('utf-8')).digest()

        user = User.passwordIsMatch(usr, hashedpwd)
        if user:
            login_user(user)
            return redirect(url_for('main_views.profilePage', userID = user.id))
        else:
            return render_template("html/login.html", error="Invalid Login")
    return render_template("html/login.html")

@main_views.route('/createAccount', methods=["GET", "POST"])
def createAccount():
    """
    View for the registration page. GET request will render the registration page in the browser,
    POST requests will be handled as a new user attempting to register based on information provided
    in the registration page's form.
    """
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
            # Input into DB with hashed password
            user = User(email=email, password=sha256((str(SALT) + password1).encode('utf-8')).digest(), dob=dob, gender=gender, preferredGym=prefGym, prefname=prefName)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main_views.welcomePage'))
        else:
            return render_template("html/createAccount.html", error = msg)

    return render_template("html/createAccount.html")

@main_views.route('/profilePage/<userID>',  methods=["GET", "POST"])
def profilePage(userID):
    """
    Page to display user profiles. If own profile, will allow user to edit. POST requests will be ratings or
    a user editing their own profile.
    """
    user = db.get_or_404(User, userID)

    #default edit
    edit = False

    #Check if it's user's own profile page or if they have rated the other user before.
    myProfilePage = user.id == current_user.id
    pairRating = Rating.getRatingFromUser(current_user.id, user.id)
    alreadyRated = pairRating is not None

    #Get Rating
    getRating = Rating.getRating(user.id)

    #HANLE POST METHOD
    if request.method == "POST":
        #Check if POST is for rating user form.
        if 'rateUser' in request.form:
            #Get Rating that was given by user
            rateUser = request.form['rateUser']
            
            #Add rating to DB
            print(rateUser)
            #pairRating = Rating.getRatingFromUser(current_user.id, user.id)
            if alreadyRated:
                pairRating.rating = rateUser
            else:
                rating = Rating(current_user.id, user.id, rateUser)
                db.session.add(rating)
            db.session.commit()
        
        #Check if POST is for toggling edit ability on user profile.
        elif 'editProf' in request.form:
            edit = request.form['editProf']  
            print(edit)
        
        #Get edited fields.
        elif 'saveEdit' in request.form:
            
            #Get updated info and add to DB
            current_user.prefName = str(request.form.get('prefName'))
            dobstr = str(request.form.get('dateOfBirth'))
            month = int(dobstr[5:7])
            day = int(dobstr[8:])
            year = int(dobstr[:4])
            current_user.dob = date(year, month, day)
            current_user.gender = str(request.form.get('gender'))
            current_user.favExerciseStr = str(request.form.get('favExercise'))
            current_user.favMusicStr = str(request.form.get('favMusic'))
            current_user.fitGoalsStr = str(request.form.get('fitGoals'))
            current_user.exFreqStr = str(request.form.get('exFreq'))
            current_user.exLengthStr = str(request.form.get('exLength'))
            current_user.warmUpsStr = str(request.form.get('warmUps'))
            current_user.spottingStr = str(request.form.get('spotting'))
            current_user.LFPartnerStr = str(request.form.get('LFPartner'))
            current_user.occupationStr = str(request.form.get('occupation'))
            current_user.hobbiesStr = str(request.form.get('hobbies'))
            db.session.commit()

    return render_template("html/profilePage.html", 
        profileHeader = user.prefname,
        uName = user.prefname, 
        prefName = user.prefname, 
        dob = str(user.dob), 
        gender = user.gender,
        prefGym = user.preferredGym,
        myPage = myProfilePage,
        rated = alreadyRated,        
        rating = getRating,
        editPage = edit,
        favExercise = user.favExerciseStr,
        favMusic = user.favMusicStr,
        fitGoals = user.fitGoalsStr,
        exFreq = user.exFreqStr,
        exLength = user.exLengthStr,
        warmUps = user.warmUpsStr,
        spotting = user.spottingStr,
        LFPartner = user.LFPartnerStr,
        occupation = user.occupationStr,
        hobbies = user.hobbiesStr
        )

@main_views.route('/welcomePage')
def welcomePage():
    return render_template("html/welcomePage.html")