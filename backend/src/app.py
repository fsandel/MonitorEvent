from flask import Flask
import json

from users import fetchUsersFromEvent
from oauth import doOauth
app = Flask(__name__)


PARTNERFAIR = 19304
oauth = doOauth()
allUsers = json.dumps([{"userName": "fsandel", "userId": '1234'}], indent=4)


@app.route("/refresh")
def refresh() -> str:
    global allUsers 
    allUsers = fetchUsersFromEvent(oauth, PARTNERFAIR)
    return "refreshed"

@app.route("/raw")
def home() -> json:
    return allUsers




def main():
  '''main function'''
  app.run(host="0.0.0.0", port=4000)

if __name__ == "__main__":
  main()
