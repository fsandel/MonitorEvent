from flask import Flask
import json

from users import fetchUsersFromEvent, fetchUserPictures
from oauth import doOauth
app = Flask(__name__)


PARTNERFAIR = 19304
oauth = doOauth()
allUsers = json.dumps([{"userName": "fsandel", "userId": '1234'}], indent=4)
allUsersPictures = [{"userName": "fsandel", "userId": '1234', 'userImg': "https://i.guim.co.uk/img/media/26392d05302e02f7bf4eb143bb84c8097d09144b/446_167_3683_2210/master/3683.jpg?width=620&dpr=1&s=none"}]


@app.route("/refresh")
def refresh() -> str:
    global allUsers 
    allUsers = fetchUsersFromEvent(oauth, PARTNERFAIR)
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
    return json.dumps(allUsersPictures, indent=4)





def main():
  '''main function'''
  app.run(host="0.0.0.0", port=4000)

if __name__ == "__main__":
  main()
