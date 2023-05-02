from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import current_user, login_required, logout_user
from models import db, User, Exercise, Message, Gym
from json import dumps
from collections import deque
from fogsaaUtil import compareSequences

userpool = dict()
notifications = dict()

auth = Blueprint('auth', __name__)

@auth.route('/findBuddy', methods=["GET", "POST"])
@login_required
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
            if val == "None" or val == "Break":
                val = None
            exerciseList.append(val)

        # Will probably have to be updated to handle the list.
        current_user.routineset = exerciseList

        if current_user.preferredGym not in userpool.keys():
            userpool[current_user.preferredGym] = dict()
        userpool[current_user.preferredGym][current_user.id] = current_user.routineset

        return redirect(url_for('auth.matchesPage'))
        
    return render_template("html/findBuddy.html", id=current_user.id, exercises=Exercise.query.all(), limit=exerciseLimit)

@auth.route('/matchesPage')
@login_required
def matchesPage():
    """
    Renders the page for user matching given the current user pool.
    """
    userHolder = list()
    gymUsers = userpool[current_user.preferredGym]
    for id in gymUsers:
        if id == current_user.id:
            continue
        userHolder.append((User.findUserByID(id), compareSequences(gymUsers[current_user.id], gymUsers[id])))
    # matches = list(map(lambda tup: User.findUserByID(tup[0]), current_user.routine_match(userpool[current_user.preferredGym])))
    return render_template("html/matchesPage.html", matches=sorted(userHolder, key=lambda match: match[1], reverse=True))

@auth.route('/messages')
@login_required
def messagesPage():
    """
    Renders the page with a list of all the user's messages.
    """
    #PLACEHOLDER
    #This section is for testing while I set up querying with SQLAlchemy
    messagepairs = []
    for message in Message.getMessageList(current_user.id):
        print(type(message))
        messagepairs.append([User.findUserByID(message.sender), message])
    return render_template("html/messageList.html", messagepairs=messagepairs)
    #END PLACEHOLDER

@auth.route('/message/<int:userID>', methods=['GET', 'POST'])
@login_required
def messagingPage(userID):
    """
    Renders the page with the conversation between the current user and one other specific user
    """
    messageList = Message.getMessagesBetweenUsers(current_user.id, userID)
    for message in messageList:
        message.seen = True
    db.session.commit()
    if request.method == 'POST':
        messageContents = request.form.get('msg')
        if messageContents.strip():
            msg = Message(current_user.id, userID, messageContents)
            db.session.add(msg)
            db.session.commit()
            notifications[userID] = "New messsage from: " + current_user.prefname
            return redirect(url_for('auth.messagingPage', userID=userID))

    return render_template('html/conversation.html', partner=User.findUserByID(userID), messageTuples=[(User.findUserByID(m.sender), m) for m in messageList])

@auth.route('/profPicUpload')
@login_required
def profPicUpload():
    return render_template("html/profPicUpload.html")

@auth.route('/getnotifications')
@login_required
def getnotifications():
    """
    Notification handler for ajax requests, will return a notification message if there is any for the current user.
    Should be rendered as an alert.
    """
    return dumps(notifications.pop(current_user.id, None))

@auth.route('/match/<int:userID>')
@login_required
def match(userID):
    try:
        userpool[current_user.preferredGym].pop(userID, None)
        userpool[current_user.preferredGym].pop(current_user.id, None)
    except:
        print("Oh no!")
    notifications[userID] = "Matched with " + current_user.prefname
    return redirect(url_for('auth.messagingPage', userID=userID))

@auth.route('/leavepool')
@login_required
def leavepool():
    userpool[current_user.preferredGym].pop(current_user.id, None)
    return redirect(url_for('main_views.profilePage', userID=current_user.id))

@auth.route('/deleteaccount')
@login_required
def deleteaccount():
    db.session.delete(current_user)
    logout_user()
    return redirect(url_for("main_vies.welcomePage"))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main_views.welcomePage"))