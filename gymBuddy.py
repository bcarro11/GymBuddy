# GROUP: Gym Buddy
# MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
# COURSE: CMSC 495:7383
# FILE: loginPage.js
# DATE: April 9, 2023

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
@app.route('/login', methods=["GET", "POST"])
def loginPage():
    if request.method == "POST":
        jsonData = request.get_json()
        print(jsonData)
        return {
            'response' : jsonData
        }
    return render_template("html/login.html")


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
def profilePage():
    return render_template("html/profilePage.html")


@app.route('/findBuddy')
def findBuddyPage():
    return render_template("html/findBuddy.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
