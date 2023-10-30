# MonitorEvent

This is a project to monitor users subscribed to an event at ecole 42

## Setup

- create an App in the 42 Intra
- create a .env file in the Root and fill it with

```
UID=<YOUR-UID>
SECRET=<YOU-SECRET>
FLASK_APP=/code/backend/src/app.py
FLASK_DEBUG=1 #if you want debug mode to be active
```

- type make in the root of the repository

## Usage

You should be able to access the main page on localhost:3000
To actual refresh the data navigate to localhost:3000/admin, choose the fitting exam and press refresh. The data refresh takes about 5-10 minutes.
To get live data you can click on a user on the homepage and another API call gets made to the 42 API that gets projects and exams.
