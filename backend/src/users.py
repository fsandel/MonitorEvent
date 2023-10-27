import json

from constants import API_URL

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