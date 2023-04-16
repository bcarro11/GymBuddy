from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import current_user
from models import User
from gymBuddy import db

auth = Blueprint('auth', __name__)

@auth.route('/findBuddy', methods=["GET", "POST"])
def findBuddy():
    cUser = current_user
    if request.method == "POST":
        exSquats = request.form.get('squats')
        exTriceps = request.form.get('triceps')
        if(exSquats):
            # MATCHING OCCURS HERE?
            return redirect(url_for('matchesPage'))
        
    return render_template("html/findBuddy.html", id = current_user.id)

@auth.route('/matchesPage')
def matchesPage():
    return render_template("html/matchesPage.html")