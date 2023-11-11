from flask import Flask, request, jsonify
import json
from flask_cors import CORS
from fetch import fetchAllUsers, grabPiscinerFromUser, getPiscinerInExam, fetchExamNamesFromUser, fetchProjectsFromUser
from oauth import doOauth
import threading
from constants import MONTH, YEAR, EXAM

app = Flask(__name__)
CORS(app, resources={
     r"*": {"origins": "*"}}, methods=["GET", "POST"])

oauth = doOauth()


allUsers = []
allPisciners = []
allPiscinersInExam = [{'userName': 'name1', 'userId': 168897, 'userImg': 'https://upload.wikimedia.org/wikipedia/commons/1/15/Cat_August_2010-4.jpg', 'pool_month': 'october', 'pool_year': '2023', 'registered': 'True'},
                      {'userName': 'name2', 'userId': 168859, 'userImg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/RedCat_8727.jpg/1200px-RedCat_8727.jpg', 'pool_month': 'october', 'pool_year': '2023', 'registered': 'False'}]


@app.route("/getexam")
def getexam() -> str:
    return jsonify({"examName": EXAM})


@app.route("/setexam", methods=["POST"])
def setexam():
    print("request json", request.get_json())
    global EXAM
    if request.method == "POST":
        try:
            data = request.get_json()
            print("data inside: ", data)
            EXAM = data
        except:
            print("something failed")
        return jsonify({"message": "exam successfully changed"})


@app.route("/getuserdata")
def pictures() -> json:
    return json.dumps(allPiscinersInExam, indent=4)


@app.route("/getmonth")
def getmonth():
    return jsonify(MONTH)


@app.route("/getyear")
def getyear():
    return jsonify(YEAR)


def background():
    global allUsers
    global allPisciners
    global allPiscinersInExam
    allUsers = fetchAllUsers(oauth)
    allPisciners = grabPiscinerFromUser(allUsers, MONTH, YEAR)
    allPiscinersInExam = getPiscinerInExam(
        oauth=oauth, examName=EXAM, allPisciner=allPisciners)


@app.route("/refresh", methods=["POST"])
def refresh():
    if request.method == "POST":
        global allUsers
        global allPisciners
        global allPiscinersInExam
        thread = threading.Thread(target=background)
        thread.daemon = True
        thread.start()
        return "worked"


def grabUserName(userId):
    global allPiscinersInExam
    for user in allPiscinersInExam:
        if user["userId"] == int(userId):
            return user["userName"]
    return "user not found"


@app.route("/user/<userId>")
def user(userId):
    userName = grabUserName(userId)
    exams = fetchExamNamesFromUser(oauth, userId)
    projects = fetchProjectsFromUser(oauth, userId)
    print(projects)
    return {"userName": userName, "exams": exams, "projects": projects}


def main():
    '''main function'''
    app.run(host="0.0.0.0", port=4000)


if __name__ == "__main__":
    main()
