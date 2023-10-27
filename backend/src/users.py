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
  return list(allUsers.values())

def fetchUserPictures(oauth, allUsers):
    allUsersPictures = []
    for user in allUsers:
        response = oauth.get(f"{API_URL}/v2/users/{user['userId']}")
        if response.status_code == 200:
          data = response.json()
          image = data["image"]["versions"]["small"]
          entry = {"userName": user['userName'], "userId": user['userId'], "userImg": image}
          allUsersPictures.append(entry)
    return allUsersPictures

