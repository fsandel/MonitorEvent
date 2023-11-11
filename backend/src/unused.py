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
            for user in data:
                allUsers[user['login']] = (
                    {"userName": user['login'], "userId": user['id']})
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
