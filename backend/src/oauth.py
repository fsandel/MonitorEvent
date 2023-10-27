import os
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from constants import API_URL

UID = os.getenv('UID')
SECRET = os.getenv('SECRET')

def doOauth():

  client = BackendApplicationClient(client_id=UID)
  oauth = OAuth2Session(client=client)
  oauth.fetch_token(
  token_url=f"{API_URL}/oauth/token", client_id=UID, client_secret=SECRET)
  return oauth