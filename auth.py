from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import current_user, login_required, logout_user
from models import db, User, Exercise, Message, Gym
from json import dumps
from collections import deque
from fogsaaUtil import compareSequences

userpool = dict()
notifications = dict()
matchrequests = dict()

auth = Blueprint('auth', __name__)

@auth.route('/findBuddy', methods=["GET", "POST"])
@login_required
def findBuddy():
    """
    Renders the view for finding a partner. Initial GET request allows you to set your exercise.
    POST requests will reroute to the matches page.
    """

    if (current_user.preferredGym in userpool.keys()) and (current_user.id in userpool[current_user.preferredGym].keys()):
        return redirect(url_for('auth.matchesPage'))

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
        score = compareSequences(gymUsers[current_user.id], gymUsers[id])
        percentMatch = int(((score / 2) / len(gymUsers[current_user.id])) * 100)
        userHolder.append((User.findUserByID(id), score, percentMatch))
    return render_template("html/matchesPage.html", matches=sorted(userHolder, key=lambda match: match[1], reverse=True), id=current_user.id)

@auth.route('/messages')
@login_required
def messagesPage():
    """
    Renders the page with a list of all the user's messages.
    """
    messagepairs = []
    for message in Message.getMessageList(current_user.id):
        print(type(message))
        messagepairs.append([User.findUserByID(message.sender), message])
    return render_template("html/messageList.html", messagepairs=messagepairs, id=current_user.id)

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
        if 'msg' in request.form:
            messageContents = request.form.get('msg')
            if messageContents.strip():
                msg = Message(current_user.id, userID, messageContents)
                db.session.add(msg)
                db.session.commit()
                notifications[userID] = {
                    'type': 'Message',
                    'message': str(current_user.prefname) + ': ' + messageContents.strip(),
                    'triggerUser': current_user.id
                }
                #"New messsage from: " + current_user.prefname
                return redirect(url_for('auth.messagingPage', userID=userID))
        elif 'confirmMatch' in request.form:
            match = request.form.get("confirmMatch")
            if match == "True":
                # Requested match
                print("REQUESTED MATCH")
                if current_user.id not in matchrequests.keys():
                    matchrequests[current_user.id] = set()
                if userID not in matchrequests.keys():
                    matchrequests[userID] = set()

                if userID in matchrequests[current_user.id]:
                    matchrequests.pop(current_user.id)
                    notifications[userID] = {
                        'type': 'Match Confirmed!',
                        'message': str(current_user.prefname) + ' has agreed to workout!',
                        'triggerUser': current_user.id
                    }
                    notifications[current_user] = {
                        'type': 'Match Confirmed!',
                        'message': str(User.findUserByID(userID).prefname) + ' has agreed to workout!',
                        'triggerUser': userID
                    }
                    userpool[current_user.preferredGym].pop(current_user.id, None)
                    userpool[current_user.preferredGym].pop(userID, None)
                else:
                    matchrequests[userID].add(current_user.id)
                    notifications[userID] = {
                        'type': 'Match Request!',
                        'message': str(current_user.prefname) + ' has requested to workout together!',
                        'triggerUser': current_user.id
                    }

            else:
                #Decided not to request match
                print("NO")

    return render_template('html/conversation.html', partner=User.findUserByID(userID), messageTuples=[(User.findUserByID(m.sender), m) for m in messageList], id=current_user.id)

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
    NOTE: Not currently implemented on front end, will be used in phase 4.
    """
    return dumps(notifications.pop(current_user.id, None))

@auth.route('/match/<int:userID>')
@login_required
def match(userID):
    """
        Middleman route which will remove both users from the queue and redirect the triggering
        user to the route to message the matched user.
        DEPRECATED
    """
    try:
        userpool[current_user.preferredGym].pop(userID, None)
        userpool[current_user.preferredGym].pop(current_user.id, None)
    except:
        print("Oh no!")
    notifications[userID] = {
        'type': 'Match',
        'message': str(current_user.prefname) + ' would like to workout!'
    }
    return redirect(url_for('auth.messagingPage', userID=userID))

@auth.route('/leavepool')
@login_required
def leavepool():
    """
        Used for a user to cancel their search and be removed from the gym pool.
    """
    userpool[current_user.preferredGym].pop(current_user.id, None)
    return redirect(url_for('main_views.profilePage', userID=current_user.id))

@auth.route('/deleteaccount')
@login_required
def deleteaccount():
    """
        Will delete the current user from the database and log them out.
        NOTE: Their messages and rating will remain. Could implement a "deleted user" style
        placeholder profile to allow people to see a user they talked to left.
    """
    print("Delete From DB: ")
    print(current_user)
    db.session.delete(current_user)
    db.session.commit()
    logout_user()
    return redirect(url_for("main_views.welcomePage"))

@auth.route('/logout')
@login_required
def logout():
    """
        Logs out the current user and redirects to the welcome page.
    """
    logout_user()
    msg = "Logged Out Successfully!"
    btn = "OK"
    return splashPage(msg, btn)
    # return redirect(url_for("main_views.login"))

@auth.route('/splashPage')
def splashPage(msg, btn):
    return render_template("html/splashPage.html", message = msg, buttonName = btn )
