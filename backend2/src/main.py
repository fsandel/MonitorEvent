'''small programm to check out intra42 api'''


# import json
from oauth import doOauth
# from users import fetchUsersFromEvent, fetchUserPictures, fetchEventInformation
# from fetch import fetchAllUsers, grabPiscinerFromUser, fetchUsersFromExam, getPiscinerInExam, fetchExamsFromUser

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

# import time
# from constants import API_URL, HEILBRONN_ID

# from app import MONTH, YEAR, EXAM

# "name": "C Piscine Exam 00",


def main():
    '''main function'''

    oauth = doOauth()
    # allUsers = fetchAllUsers(oauth)
    # # print(allUsers)
    # allPisciners = grabPiscinerFromUser(allUsers, MONTH, YEAR)
    # # print(allPisciners)
    # allPiscinersInExam = getPiscinerInExam(
    #     oauth=oauth, allPisciner=allPisciners, examName=EXAM)
    # print(allPiscinersInExam)
    # var = fetchExamsFromUser(oauth, FSANDELID)
    # print(json.dumps(var, indent=4))
    # allUsers = fetchUsersFromEvent(oauth, PARTNERFAIR)
    # allUsers = fetchUsersFromEvent(oauth, PARTNERFAIR)
    # print(allUsers)
    # allUsersPictures = fetchUserPictures(oauth, allUsers)
    # eventInformation = fetchEventInformation(oauth, PARTNERFAIR)
    # allPisciners = fetchAllPisciners(oauth)
    # piscinererInExam = getPiscinerInExam(
    #     oauth, allPisciners, "C Piscine Exam 01")
    # print(json.dumps(piscinererInExam, indent=4))
    # for i in range(10):
    #     if isUserInExam(oauth, allPisciners[i]['userId'], "C Piscine Exam 01"):
    #         print(f"{allPisciners[i]['userName']} is in exam")
    #     else:
    #         print(f"{allPisciners[i]['userName']} is not in exam")

    # print(json.dumps(fetchExamsFromUser(
    #     oauth, allPisciners[i]['userId']), indent=4))


if __name__ == "__main__":
    main()
