from flask import Flask, request, jsonify
import json
from flask_cors import CORS
import sys
from users import fetchUsersFromEvent, fetchUserPictures, fetchEventInformation
from fetch import fetchAllUsers, fetchUsersFromExam, grabPiscinerFromUser, getPiscinerInExam
from oauth import doOauth
import threading


app = Flask(__name__)
CORS(app, resources={
     r"*": {"origins": "*"}}, methods=["GET", "POST"])

PARTNERFAIR = 19304
EVENT = PARTNERFAIR
oauth = doOauth()

EXAM = "C Piscine Exam 01"
MONTH = "october"
YEAR = "2023"

allUsers = []
allPisciners = []
allPiscinersInExam = [{'userName': 'iwysocki', 'userId': 168897, 'userImg': 'https://cdn.intra.42.fr/users/23553708e7288a4edfb65aebf3d30aef/iwysocki.jpg', 'pool_month': 'october', 'pool_year': '2023', 'registered': 'True'},
                      {'userName': 'ogjaka', 'userId': 168859, 'userImg': 'https://cdn.intra.42.fr/users/e89d4476fd98b0f0c172a9c9aa318d37/ogjaka.jpg', 'pool_month': 'october', 'pool_year': '2023', 'registered': 'False'}]


@app.route("/refresh")
def refresh() -> str:
    global allUsers
    allUsers = fetchUsersFromEvent(oauth, EVENT)
    return "refreshed"


@app.route("/refreshpictures")
def refreshPictures() -> str:
    global allUsersPictures
    allUsersPictures = fetchUserPictures(oauth, allUsers)
    return "refreshed"


@app.route("/raw")
def raw() -> json:
    return json.dumps(allUsers, indent=4)


@app.route("/geteventid")
def geteventid() -> json:
    return str(EVENT)


@app.route("/geteventinformation")
def geteventinformation() -> json:
    eventInformation = fetchEventInformation(oauth, EVENT)
    return eventInformation


@app.route("/pictures")
def pictures() -> json:
    localPictures = allPiscinersInExam
    return json.dumps(localPictures, indent=4)


@app.route("/event", methods=["POST"])
def event():
    global EVENT
    if request.method == "POST":
        try:
            data = request.get_json()
            EVENT = data["eventId"]
            print(EVENT, file=sys.stderr)
        except:
            print("something failed")
        return jsonify({"message": "POST request successful"})


def background():
    global allUsers
    global allPisciners
    global allPiscinersInExam
    allUsers = fetchAllUsers(oauth)
    allPisciners = grabPiscinerFromUser(allUsers, MONTH, YEAR)
    allPiscinersInExam = getPiscinerInExam(
        oauth=oauth, examName=EXAM, allPisciner=allPisciners)


@app.route("/setup", methods=["POST"])
def setup():
    if request.method == "POST":
        global allUsers
        global allPisciners
        global allPiscinersInExam
        thread = threading.Thread(target=background)
        thread.daemon = True
        thread.start()
        return "worked"


def main():
    '''main function'''
    app.run(host="0.0.0.0", port=4000)


if __name__ == "__main__":
    main()
