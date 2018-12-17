#Spreadsheet : https://docs.google.com/spreadsheets/d/1-wkzWGS_imDF4cvg2bMmzzlFqHfpOxhSBWrnoZRdTx4/edit#gid=0
#Calender1 : 



from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
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


    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)

    service = build('calendar', 'v3', http=creds.authorize(Http()))

    page_token = None
    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        for calendar_list_entry in calendar_list['items']:
                                    print( calendar_list_entry.items())
                                    print()
                                    print()
        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')

    calendar = service.calendars().get(calendarId='dvskha@gmail.com').execute()
    for j in range(2,len(sheet.col_values(2))):
      event = {
  'summary':  calendar['summary'],
  "foreround":  sheet.row_values(j)[17],
  'location': sheet.row_values(j)[9],
  'description': "Note:" + sheet.row_values(j)[8]+ " \nProcedure:"+ sheet.row_values(j)[0]+ " \nSurgery:"+ sheet.row_values(j)[1]+ " \n Patient:"+ sheet.row_values(j)[2]+ " \n DOB:"+sheet.row_values(j)[3]+ "\n medical record number : "+sheet.row_values(j)[4]+"\n consultant:" + sheet.row_values(j)[5] + "\n residents",
  'start': {
    'dateTime': str(sheet.row_values(j)[10])+'T'+str(str(sheet.row_values(2)[12])+":00-"+str(sheet.row_values(2)[13])),
    'timeZone': 'Asia/Riyadh',
  },
  'end': {
    'dateTime': str(sheet.row_values(j)[11])+'T'+str(str(sheet.row_values(2)[12])+":00-"+str(sheet.row_values(2)[13])),
    'timeZone': 'Asia/Riyadh',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'attendees': [
    {'email': "dvskha@gmail.com"},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'popup', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

    
      event = service.events().insert(calendarId='dvskha@gmail.com', body=event).execute()

      print('Event created: %s' % (event.get('htmlLink')))
      sheet.update_cell(j, 20, event.get('htmlLink'))


if __name__ == '__main__':
    main()