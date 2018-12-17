from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_url(
            "https://docs.google.com/spreadsheets/d/1-wkzWGS_imDF4cvg2bMmzzlFqHfpOxhSBWrnoZRdTx4/edit#gid=0").get_worksheet(
            0)

    name = 'you'
    nominee = 'nominee_name'
    relation = 'relation'
    r = 0

    print(sheet.row_values(2))
    print(sheet.col_values(16))

    from oauth2client import file, client, tools
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)

    service = build('calendar', 'v3', http=creds.authorize(Http()))

    """# Call the Calendar API
                now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
                print('Getting the upcoming 10 events')
                events_result = service.events().list(calendarId='ta72bu08jc4qe6g50dnk22lj44@group.calendar.google.com', timeMin=now,
                                                    maxResults=10, singleEvents=True,
                                                    orderBy='startTime').execute()
                events = events_result.get('items', [])
            
                if not events:
                    print('No upcoming events found.')
                for event in events:
                    start = event['start'].get('dateTime', event['start'].get('date'))
                    print(start, event['summary'])"""

    calendar = service.calendars().get(calendarId='ta72bu08jc4qe6g50dnk22lj44@group.calendar.google.com').execute()

    #print(calendar['summary'])

    rown = sheet.row_values(2)
    print()
    print(str(sheet.row_values(2)[10])+'T'+str(str(sheet.row_values(2)[12])+":00-"+str(sheet.row_values(2)[13])))

    event = {
  'summary': calendar['summary'],
  "background": sheet.row_values(2)[17],
      "foreground": "white",
  'location': rown[9],
  'description': sheet.row_values(2)[8],
  'start': {
    'dateTime': str(sheet.row_values(2)[10])+'T'+str(str(sheet.row_values(2)[12])+":00-"+str(sheet.row_values(2)[13])),
    'timeZone': 'Asia/Kolkata',
  },
  'end': {
    'dateTime': str(sheet.row_values(2)[11])+'T'+str(str(sheet.row_values(2)[12])+":00-"+str(sheet.row_values(2)[13])),
    'timeZone': 'Asia/Kolkata',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'attendees': [
    {'name': [sheet.row_values(2)[2]]},
    {'email': ["abdulelah99@gmail.com"]},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': "pop up", 'minutes': 24 * 60},
      {'method': "pop up", 'minutes': 10},
    ],
  },
}

    if sheet.row_values(2)[15] == "yes":
        service.calendars().delete(calendarId='ta72bu08jc4qe6g50dnk22lj44@group.calendar.google.com').execute()
        event = service.events().insert(calendarId='ta72bu08jc4qe6g50dnk22lj44@group.calendar.google.com', body=event).execute()
    else:
        event = service.events().insert(calendarId='ta72bu08jc4qe6g50dnk22lj44@group.calendar.google.com', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))

    page_token = None
    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        """for calendar_list_entry in calendar_list['items']:
                                    print( calendar_list_entry.items())
                                    print()
                                    print()"""
        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break

if __name__ == '__main__':
    main()