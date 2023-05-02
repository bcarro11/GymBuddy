# GROUP: Gym Buddy
# MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
# COURSE: CMSC 495:7383
# FILE: gymBuddy.py
# DATE: April 9, 2023

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login.login_manager import LoginManager
from flask_login import current_user
from models import User, Exercise, db
from dotenv import load_dotenv
from os import getenv

import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

# Profile Picture Upload location
UPLOAD_FOLDER = './static/profPics/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

#Load in enviornment variables held by .env
load_dotenv()

#Initialize app with appropriate configuration such as database location and secret key value
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gymbuddy.db"
app.config["SECRET_KEY"] = getenv('SECRET_KEY')
db.init_app(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Attach the default login manager to the flask server
login_manager = LoginManager()
login_manager.init_app(app)

#Imports our views from their respective files
from main_views import main_views
app.register_blueprint(main_views)
from auth import auth
app.register_blueprint(auth)

# Instructs flask-login how to retrieve a user
@login_manager.user_loader
def load_user(user_id):
    # return User.get(user_id)
    return User.findUserByID(user_id)

#Starts application on port 5000, debug needs to be off for production
if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=True, port=5000)
