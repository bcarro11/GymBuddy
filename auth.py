from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import current_user
from models import db, User, Exercise
from collections import deque

userpool = dict()

auth = Blueprint('auth', __name__)

@auth.route('/findBuddy', methods=["GET", "POST"])
def findBuddy():
    """
    Renders the view for finding a partner. Initial GET request allows you to set your exercise.
    POST requests will reroute to the matches page.
    """

    # Sets limit on number of exercises in routine.
    exerciseLimit = 12

    if request.method == "POST":
        
        # Gets a generator(dict) of all exercises
        exerciseGenerator = request.form.items()

        # Converts the values into a list
        # Index should be order of exercise (e.g., index 0 = first exercise in routine)
        exerciseList = list()
        for key, val in exerciseGenerator:
            exerciseList.append(val)

        # Will probably have to be updated to handle the list.
        current_user.routineset = set()
        for exercise in Exercise.query.all():
            print(exercise)
            if request.form.get(exercise.name):
                current_user.routineset.add(exercise.name)

        userpool[current_user.id] = current_user.routineset

        return redirect(url_for('auth.matchesPage'))
        
    return render_template("html/findBuddy.html", id=current_user.id, exercises=Exercise.query.all(), limit=exerciseLimit)

@auth.route('/matchesPage')
def matchesPage():
    """
    Renders the page for user matching given the current user pool.
    """
    matches = list(map(lambda tup: User.findUserByID(tup[0]), current_user.routine_match(userpool)))
    print(matches)
    return render_template("html/matchesPage.html", matches=list(map(lambda tup: User.findUserByID(tup[0]), current_user.routine_match(userpool))))

