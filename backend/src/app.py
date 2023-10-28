from flask import Flask, request, jsonify
import json
from flask_cors import CORS
import sys
from users import fetchUsersFromEvent, fetchUserPictures
from oauth import doOauth
import threading


app = Flask(__name__)
CORS(app, resources={
     r"*": {"origins": "*"}}, methods=["GET", "POST"])

PARTNERFAIR = 19304
EVENT = PARTNERFAIR
oauth = doOauth()


allUsers = []
allUsersPictures = []


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


@app.route("/pictures")
def pictures() -> json:
    localPictures = allUsersPictures
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
    global allUsersPictures
    allUsers = fetchUsersFromEvent(oauth, EVENT)
    allUsersPictures = fetchUserPictures(oauth, allUsers)


@app.route("/setup", methods=["POST"])
def setup():
    if request.method == "POST":
        global allUsers
        global allUsersPictures
        thread = threading.Thread(target=background)
        thread.daemon = True
        thread.start()
        return "worked"


def main():
    '''main function'''
    app.run(host="0.0.0.0", port=4000)


if __name__ == "__main__":
    main()
