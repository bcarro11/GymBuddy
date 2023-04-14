# GROUP: Gym Buddy
# MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
# COURSE: CMSC 495:7383
# FILE: gymBuddy.py
# DATE: April 9, 2023

from flask import Flask, render_template, request, flash
from flask_login.login_manager import LoginManager

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)



class User():
    user_id = 1
    username = 'brenden'
    password = 'test123'
    name = 'brenden carroll'
    nname = 'bc'
    dob = '5/5/5'
    gender = 'male'


@login_manager.user_loader
def load_user(user_id):
    # return User.get(user_id)
    return User


@app.route('/', methods=["GET", "POST"])
@app.route('/login', methods=["GET", "POST"])
def loginPage():
    if request.method == "POST":
        usr = request.form.get('uname')
        pwd = request.form.get('psw')

        if (usr == User.username and pwd == User.password):
            return profilePage(User.username)
        else:
            return render_template("html/login.html", error="Invalid Login")
    return render_template("html/login.html")

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
        jsonData = request.get_json()
        print(jsonData)
        return {
            'response' : jsonData
        }
    return render_template("html/createAccount.html")


@app.route('/profilePage')
def profilePage(name):
    return render_template("html/profilePage.html", test=name + "'s",
        uName=User.name, nname=User.nname, dob=User.dob, gender=User.gender)


@app.route('/findBuddy')
def findBuddyPage():
    return render_template("html/findBuddy.html")

if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=True, port=5000)
