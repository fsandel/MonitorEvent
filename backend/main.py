'''small programm to check out intra42 api'''

# import env
# from check_out_user import check_out_user
# from all_users import all_user_data
# from dotenv import load_dotenv
import os
import json

import sys
import subprocess
import os
import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
# from PIL import Image


# load_dotenv()

UID = os.getenv('UID')
SECRET = os.getenv('SECRET')

API_URL = "https://api.intra.42.fr"


def doOauth():

  client = BackendApplicationClient(client_id=UID)
  oauth = OAuth2Session(client=client)
  oauth.fetch_token(
  token_url=f"{API_URL}/oauth/token", client_id=UID, client_secret=SECRET)
  return oauth

def fetchMe(oauth):
  FSANDELID = 112576
  PARTNERFAIR = 19304

  response = oauth.get(f"{API_URL}/v2/events/{PARTNERFAIR}/users?page=5")
  # response = oauth.get(f"{API_URL}/v2/users/{FSANDELID}/events")

  if (response.status_code == 200):
    data = response.json()
    pretty = json.dumps(data, indent = 4)
    print(pretty)
  else:
    print(f"statuscode: {response.status_code}")

def removeduplicate(it):
  seen = []
  for x in it:
    if x not in seen:
      yield x
      seen.append(x)

def fetchUsersFromEvent(oauth, event_id):
  amount = 1
  page = 0
  allUsers = {}
  while amount > 0:
    response = oauth.get(f"{API_URL}/v2/events/{event_id}/users?page={page}")
    if response.status_code == 200:
      page += 1
      data = response.json()
      for user in data:
        allUsers[user['login']] = ({"userName": user['login'], "userId": user['id']})
      amount = len(data)
    else:
      amount = 0
  return json.dumps(list(allUsers.values()), indent=4)

def main():
    '''main function'''
    FSANDELID = 112576
    PARTNERFAIR = 19304
    oauth = doOauth()
    allUsers = fetchUsersFromEvent(oauth, PARTNERFAIR)
    print(allUsers)

if __name__ == "__main__":
    main()
