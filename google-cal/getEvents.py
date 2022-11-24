# Utils imports
import json
import datetime
import os.path
import time
# Google imports
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
service = build('calendar', 'v3', credentials=creds)

# Calendar IDs
calendarIdList = [
    'primary',
    'cadsvskbdp4b4a5njoeh4lp314@group.calendar.google.com',
    '0eumcrv5gkahhq8o98uej4ame8@group.calendar.google.com'
]

# Folds
yearList = [2017,2018,2019,2020,2021,2022]
monthList = ["01","02","03","04","05","06","07","08","09","10","11","12"]
timeList = {}
for year in yearList:
    for i, month in enumerate(monthList):
        if i == 11:
            timeList[f"{year}_{month}"] = [f"{year}-{month}-01T00:00:00-05:00", f"{year}-{month}-31T23:59:59-05:00"]
        else: 
            timeList[f"{year}_{month}"] = [f"{year}-{month}-01T00:00:00-05:00", f"{year}-{monthList[i+1]}-01T00:00:00-05:00"]

# Save all calendar events in separate JSON
for key in timeList:
    for calendarId in calendarIdList:
        # Create request for date in range
        request = service.events().list(
            calendarId=calendarId, 
            singleEvents=True, 
            orderBy='startTime', 
            timeMin=timeList[key][0], 
            timeMax=timeList[key][1]
        )
        try:
            response = request.execute()
            events = response.get('items', [])
            if not events:
                print('No events found in',key,calendarId)
            response_json = json.dumps(response, indent=2)
            if not os.path.exists(f"data/{calendarId}"):
                os.makedirs(f"data/{calendarId}")
            with open(f"data/{calendarId}/{key}_{calendarId}.json", "w") as outfile:
                outfile.write(response_json)
        except HttpError as error:
            print('An error occurred: %s' % error)

# Shutdown
service.close()