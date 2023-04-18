from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import current_user
from models import db, User, Exercise

userpool = dict()

auth = Blueprint('auth', __name__)

@auth.route('/findBuddy', methods=["GET", "POST"])
def findBuddy():
    if request.method == "POST":
        exSquats = request.form.get('squats')
        exTriceps = request.form.get('triceps')
        current_user.routineset = set()
        for exercise in Exercise.query.all():
            print(exercise)
            if request.form.get(exercise.name):
                current_user.routineset.add(exercise.name)

        userpool[current_user.id] = current_user.routineset

        return redirect(url_for('auth.matchesPage'))
        
    return render_template("html/findBuddy.html", id=current_user.id, exercises=Exercise.query.all())

@auth.route('/matchesPage')
def matchesPage():
    matches = list(map(lambda tup: User.findUserByID(tup[0]), current_user.routine_match(userpool)))
    print(matches)
    return render_template("html/matchesPage.html", matches=list(map(lambda tup: User.findUserByID(tup[0]), current_user.routine_match(userpool))))