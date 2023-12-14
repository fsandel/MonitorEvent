import time
from constants import API_URL, HEILBRONN_ID


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


def fetchAllUsers(oauth, returnUsers):
    returnUsers.clear()
    amount = 1
    page = 0
    while amount > 0:
        time.sleep(1)
        response = oauth.get(
            f"{API_URL}/v2/campus/{HEILBRONN_ID}/users?page={page}")
        if response.status_code == 200:
            page += 1
            data = response.json()
            for user in data:
                returnUsers.append({"userName": user['login'], "userId": user['id'], "userImg": user['image']
                                   ['link'], "pool_month": user['pool_month'], "pool_year": user['pool_year']})
            amount = len(data)
        else:
            amount = 0


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


def getPiscinerInExam(oauth, allPisciner, examName, piscinerInExam):
    piscinerInExam.clear()
    for pisciner in allPisciner:
        if isUserInExam(oauth, pisciner['userId'], examName):
            pisciner['registered'] = "True"
        else:
            pisciner['registered'] = "False"
        piscinerInExam.append(pisciner)


def fetchUserPictures(oauth, allUsers):
    allUsersPictures = []
    print(len(allUsers))
    for user in allUsers:
        time.sleep(1)
        response = oauth.get(f"{API_URL}/v2/users/{user['userId']}")
        if response.status_code == 200:
            data = response.json()
            image = data["image"]["versions"]["small"]
            entry = {"userName": user['userName'],
                     "userId": user['userId'], "userImg": image}
            allUsersPictures.append(entry)
    return allUsersPictures
