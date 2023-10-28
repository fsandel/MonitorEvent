'''small programm to check out intra42 api'''


import json
from oauth import doOauth
from users import fetchUsersFromEvent, fetchUserPictures, fetchEventInformation


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

import time
from constants import API_URL, HEILBRONN_ID


def fetchAllEvents(oauth):
    amount = 1
    page = 0
    allEvents = {}
    while amount > 0:
        time.sleep(1)
        response = oauth.get(
            f"{API_URL}/v2/campus/{HEILBRONN_ID}/events?page={page}")
        if response.status_code == 200:
            page += 1
            data = response.json()
            for event in data:
                allEvents[event['id']] = {
                    "eventId": event['id'], "eventName": event['name'], "begin": event['begin_at'], "end": event['end_at']}
            amount = len(data)
        else:
            amount = 0
    return list(allEvents.values())


def fetchAllExams(oauth):
    amount = 1
    page = 0
    allExams = {}
    while amount > 0:
        time.sleep(1)
        response = oauth.get(
            f"{API_URL}/v2/campus/{HEILBRONN_ID}/exams?page={page}")
        if response.status_code == 200:
            page += 1
            data = response.json()
            return data
            for event in data:
                allExams[event['id']] = {
                    "eventId": event['id'], "eventName": event['name'], "begin": event['begin_at'], "end": event['end_at']}
            amount = len(data)
        else:
            amount = 0
    return list(allExams.values())


def fetchUsersFromExam(oauth, event_id):
    amount = 1
    page = 0
    allUsers = {}
    while amount > 0:
        time.sleep(1)
        response = oauth.get(
            f"{API_URL}/v2/exams/{event_id}/users?page={page}")
        if response.status_code == 200:
            page += 1
            data = response.json()
            return data
            for user in data:
                allUsers[user['login']] = (
                    {"userName": user['login'], "userId": user['id']})
            amount = len(data)
        else:
            amount = 0
    return list(allUsers.values())


def fetchExamsFromUser(oauth, userId):
    amount = 1
    page = 0
    allUsers = {}
    while amount > 0:
        time.sleep(1)
        response = oauth.get(
            f"{API_URL}/v2/users/{userId}/exams?page={page}")
        if response.status_code == 200:
            page += 1
            data = response.json()
            for exam in data:
                allUsers[exam['id']] = exam
            amount = len(data)
        else:
            amount = 0
    return list(allUsers.values())


def fetchAllCampus(oauth):
    response = oauth.get(
        f"{API_URL}/v2/campus")
    if response.status_code == 200:
        data = response.json()
        return data


def fetchAllPisciners(oauth):
    amount = 1
    page = 0
    allUsers = {}
    year = "2023"
    month = "october"
    while amount > 0:
        time.sleep(1)
        response = oauth.get(
            f"{API_URL}/v2/campus/{HEILBRONN_ID}/users?page={page}")
        if response.status_code == 200:
            page += 1
            data = response.json()
            for user in data:
                if user['pool_month'] == month and user['pool_year'] == year:
                    allUsers[user['login']] = (
                        {"userName": user['login'], "userId": user['id'], "userImg": user['image']['link']})
            amount = len(data)
        else:
            amount = 0
    return list(allUsers.values())


def isUserInExam(oauth, userId, examName):
    allExams = fetchExamsFromUser(oauth, userId)
    for exam in allExams:
        if exam['name'] == examName:
            return True
    else:
        return False


def getPiscinerInExam(oauth, allPisciner, examName):
    piscinerInExam = []
    for pisciner in allPisciner:
        if isUserInExam(oauth, pisciner['userId'], examName):
            piscinerInExam.append(pisciner)
    return piscinerInExam


# "name": "C Piscine Exam 00",
def main():
    '''main function'''
    FSANDELID = 112576
    PARTNERFAIR = 19304
    oauth = doOauth()
    # allUsers = fetchUsersFromEvent(oauth, PARTNERFAIR)
    # allUsers = fetchUsersFromEvent(oauth, PARTNERFAIR)
    # print(allUsers)
    # allUsersPictures = fetchUserPictures(oauth, allUsers)
    # eventInformation = fetchEventInformation(oauth, PARTNERFAIR)
    allPisciners = fetchAllPisciners(oauth)
    piscinererInExam = getPiscinerInExam(
        oauth, allPisciners, "C Piscine Exam 01")
    print(json.dumps(piscinererInExam, indent=4))
    # for i in range(10):
    #     if isUserInExam(oauth, allPisciners[i]['userId'], "C Piscine Exam 01"):
    #         print(f"{allPisciners[i]['userName']} is in exam")
    #     else:
    #         print(f"{allPisciners[i]['userName']} is not in exam")

    # print(json.dumps(fetchExamsFromUser(
    #     oauth, allPisciners[i]['userId']), indent=4))


if __name__ == "__main__":
    main()
