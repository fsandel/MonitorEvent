'''small programm to check out intra42 api'''

# import env
# from check_out_user import check_out_user
# from all_users import all_user_data
from dotenv import load_dotenv
import os
import json

import sys
import subprocess
import os
import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from PIL import Image


load_dotenv()

UID = os.getenv('UID')
SECRET = os.getenv('SECRET')

API_URL = "https://api.intra.42.fr"


def doOauth():

  client = BackendApplicationClient(client_id=UID)
  oauth = OAuth2Session(client=client)
  oauth.fetch_token(
  token_url=f"{API_URL}/oauth/token", client_id=UID, client_secret=SECRET)
  return oauth

    # "id": 19304,
    # "event_id": 287,
    # "user_id": 14933,
    # "user": {
    #     "id": 14933,
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

def fetchUsersFromEvent(oauth, event_id):
  amount = 1
  page = 0
  while amount > 0:
    response = oauth.get(f"{API_URL}/v2/events/{event_id}/users?page={page}")
    if response.status_code == 200:
      page += 1
      data = response.json()
      for user in data:
        print(f"{user['login']},{user['id']}")
      # print(len(data))
      # pretty = json.dumps(data, indent = 4)
      amount = len(data)
      # print(pretty)
    else:
      amount = 0

def main():
    '''main function'''
    FSANDELID = 112576
    PARTNERFAIR = 19304
    # print(os.getenv('UID'))
    oauth = doOauth()
    # fetchMe(oauth)
    fetchUsersFromEvent(oauth, PARTNERFAIR)
    # all_user_data(UID, SECRET)


if __name__ == "__main__":
    main()
