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
    creds = ServiceAccountCredentials.from_json_keyfile_name('sync/client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_url(
            "https://docs.google.com/spreadsheets/d/1Q0OopBJjl5WuxeRNlqpi1V-RGl6PuZbqioPL85bJeSw/edit#gid=0").get_worksheet(
            0)1

    name = 'you'
    nominee = 'nominee_name'
    relation = 'relation'
    r = 0


    from oauth2client import file, client, tools
    store = file.Storage('sync/token.json')
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


    for j in range(2,len(sheet.col_values(2))+1):
        colorid = 1
        if str(sheet.row_values(j)[17]) == "Green":
          colorid = 3
        if str(sheet.row_values(j)[17]) == "Blue":
          colorid = 1
        if str(sheet.row_values(j)[17]) == "Red":
          colorid = 4
        if str(sheet.row_values(j)[17]) == "Orange":
          colorid = 6
        if str(sheet.row_values(j)[17]) == "Black":
          colorid = 8
        print(j)
        print(str(sheet.row_values(j)[15]))
        print(str(sheet.row_values(j)[18]))
        event1 = {
  'summary':  'summary',
  "colorId": colorid,
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


        calendarId_record = 'dtfcbt1a37od6hgljl24t96r74@group.calendar.google.com'
        calendarId_surgeries='3l7etudrleq31c82l2mlgfrddg@group.calendar.google.com'
        calendarId_important = 'ri5l7up5u0taqlka6d3cv38gf8@group.calendar.google.com'

        if str(sheet.row_values(j)[15])=="yes" and str(sheet.row_values(j)[18])!="Cancelledcallender":
          sheet.update_cell(j, 20, "-")
          sheet.update_cell(j, 21, "-")
          event_s = service.events().insert(calendarId='3l7etudrleq31c82l2mlgfrddg@group.calendar.google.com', body=event1).execute()
          event_id= event_s.get('id')
          service.events().delete(calendarId=calendarId_surgeries , eventId=event_id ).execute()

          event = service.events().insert(calendarId='3l7etudrleq31c82l2mlgfrddg@group.calendar.google.com', body=event1).execute()
          print('Event created: %s' % (event.get('htmlLink')))
          event_id= print(event.get('id'))
          sheet.update_cell(j, 19, "Cancelledcallender")
          sheet.update_cell(j, 20, event.get('htmlLink'))
          sheet.update_cell(j, 21, event.get('id'))

          if str(sheet.row_values(j)[18])=="Important":
            updated_event = service.events().move(
            calendarId=calendarId_important, eventId='eventId',
            destination=calendarId_record.execute())
          
          if str(sheet.row_values(j)[18])=="Democalender":
            updated_event = service.events().move(
            calendarId=calendarId_surgeries, eventId='eventId',
            destination=calendarId_record.execute())

        elif str(sheet.row_values(j)[15])=="no" and str(sheet.row_values(j)[18])=="Important":
          event = service.events().insert(calendarId=calendarId_important, body=event1).execute()
          print('Event created: %s' % (event.get('htmlLink')))
          event_id= print(event.get('id'))
          sheet.update_cell(j, 20, event.get('htmlLink'))
          sheet.update_cell(j, 21, event.get('id'))
          # Print the updated date.

        elif str(sheet.row_values(j)[15])=="no" and str(sheet.row_values(j)[18])=="Democalender":
          event = service.events().insert(calendarId=calendarId_surgeries, body=event1).execute()
          print('Event created: %s' % (event.get('htmlLink')))
          event_id= print(event.get('id'))
          sheet.update_cell(j, 20, event.get('htmlLink'))
          sheet.update_cell(j, 21, event.get('id'))
          # Print the updated date.

        else:
          print(sheet.row_values(j)[15])
          print(sheet.row_values(j)[18])
          print("What is wrongs")

if __name__ == '__main__':
    main()