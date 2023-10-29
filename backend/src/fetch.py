import time
import json
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


def fetchExamNamesFromUser(oauth, userId):
    amount = 1
    page = 0
    allExams = {}
    while amount > 0:
        time.sleep(1)
        response = oauth.get(
            f"{API_URL}/v2/users/{userId}/exams?page={page}")
        if response.status_code == 200:
            page += 1
            data = response.json()
            for exam in data:
                allExams[exam['id']] = exam
            amount = len(data)
        else:
            amount = 0
    examList = list(allExams.values())
    examNameList = []
    for exam in examList:
        examNameList.append(exam["name"])
    return examNameList


def fetchProjectsFromUser(oauth, userId):
    amount = 1
    page = 0
    allUsers = {}
    while amount > 0:
        time.sleep(1)
        response = oauth.get(
            f"{API_URL}/v2/users/{userId}/projects_users?page={page}")
        if response.status_code == 200:
            page += 1
            data = response.json()
            for exam in data:
                allUsers[exam['project']['name']] = exam['project']['name']
            amount = len(data)
        else:
            print("failed")
            amount = 0
    return list(allUsers.values())


def fetchAllCampus(oauth):
    response = oauth.get(
        f"{API_URL}/v2/campus")
    if response.status_code == 200:
        data = response.json()
        return data


def fetchAllUsers(oauth):
    amount = 1
    page = 0
    allUsers = {}
    while amount > 0:
        time.sleep(1)
        response = oauth.get(
            f"{API_URL}/v2/campus/{HEILBRONN_ID}/users?page={page}")
        if response.status_code == 200:
            page += 1
            data = response.json()
            for user in data:
                allUsers[user['login']] = (
                    {"userName": user['login'], "userId": user['id'], "userImg": user['image']['link'], "pool_month": user['pool_month'], "pool_year": user['pool_year']})
            amount = len(data)
        else:
            amount = 0
    return list(allUsers.values())


def grabPiscinerFromUser(allUsers, month, year):
    allPisciner = []
    for user in allUsers:
        if user['pool_month'] == month and user['pool_year'] == year:
            allPisciner.append(user)
    return allPisciner


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
            pisciner['registered'] = "True"
        else:
            pisciner['registered'] = "False"
    return allPisciner
