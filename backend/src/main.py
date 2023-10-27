'''small programm to check out intra42 api'''


from oauth import doOauth
from users import fetchUsersFromEvent





# def fetchMe(oauth):
#   FSANDELID = 112576
#   PARTNERFAIR = 19304

#   response = oauth.get(f"{API_URL}/v2/events/{PARTNERFAIR}/users?page=5")
#   # response = oauth.get(f"{API_URL}/v2/users/{FSANDELID}/events")

#   if (response.status_code == 200):
#     data = response.json()
#     pretty = json.dumps(data, indent = 4)
#     print(pretty)
#   else:
#     print(f"statuscode: {response.status_code}")



def main():
    '''main function'''
    FSANDELID = 112576
    PARTNERFAIR = 19304
    oauth = doOauth()
    allUsers = fetchUsersFromEvent(oauth, PARTNERFAIR)
    print(allUsers)

if __name__ == "__main__":
    main()