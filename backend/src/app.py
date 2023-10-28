from flask import Flask, request, jsonify
import json
from flask_cors import CORS
import sys
from users import fetchUsersFromEvent, fetchUserPictures
from oauth import doOauth
app = Flask(__name__)
CORS(app, resources={
     r"*": {"origins": "http://localhost:3000"}}, methods=["GET", "POST"])

PARTNERFAIR = 19304
EVENT = 19304
oauth = doOauth()
# allUsers = [{"userName": "fsandel", "userId": '1234'},
#             {"userName": "fsandel", "userId": '1234'}]
# allUsersPictures = [{"userName": "fsandel", "userId": '1234',
#                      'userImg': "https://i.guim.co.uk/img/media/26392d05302e02f7bf4eb143bb84c8097d09144b/446_167_3683_2210/master/3683.jpg?width=620&dpr=1&s=none"}]

allUsers = fetchUsersFromEvent(oauth, EVENT)
allUsersPictures = fetchUserPictures(oauth, allUsers)


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


# @app.route("/setup", methods=["POST"])
# async def setup():
#     if request.method == "POST":
#         global allUsers
#         global allUsersPictures
#         allUsers = fetchUsersFromEvent(oauth, EVENT)
#         allUsersPictures = await fetchUserPictures(oauth, allUsers)
#         return jsonify({"message": "POST request successful"})


# @app.route("/setup", methods=["POST"])
# def setup():
    # if request.method == "POST":

        # Define a function to run fetchUserPictures in a separate thread

def background():
    global allUsers
    global allUsersPictures
    allUsers = fetchUsersFromEvent(oauth, EVENT)
    allUsersPictures = fetchUserPictures(oauth, allUsers)
    print("start background task")
    print("start background task", file=sys.stderr)

    # Create and start a new thread for fetchUserPictures

    # Return an immediate response to the client
    # return jsonify({"message": "Fetching user pictures in the background"})


def main():
    '''main function'''
    app.run(host="0.0.0.0", port=4000)


if __name__ == "__main__":
    main()
