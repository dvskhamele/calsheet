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
    """sheet = client.open_by_url(
                        "https://docs.google.com/spreadsheets/d/1Q0OopBJjl5WuxeRNlqpi1V-RGl6PuZbqioPL85bJeSw/edit#gid=0").get_worksheet(
                        0)
            """
    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1Mopww1jcxLWRd06kZIIO1Ow9S9goi8yhwjM6pOUZ_Jk/edit#gid=0").get_worksheet(
            0)

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

    """page_token = None
                while True:
                    calendar_list = service.calendarList().list(pageToken=page_token).execute()
                    for calendar_list_entry in calendar_list['items']:
                                                print(calendar_list_entry.items())
                                                print()
                                                print()
                    page_token = calendar_list.get('nextPageToken')
                    if not page_token:
                        break
            """
##############################################Start from here#############################################

        
    calendarId_record = 'dtfcbt1a37od6hgljl24t96r74@group.calendar.google.com'
    calendarId_surgeries='3l7etudrleq31c82l2mlgfrddg@group.calendar.google.com'
    calendarId_important = 'ri5l7up5u0taqlka6d3cv38gf8@group.calendar.google.com'
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    page_token = None
    while True:
      events = service.events().list(calendarId=calendarId_surgeries, pageToken=page_token).execute()
      for event in events['items']:
        events_u=(event['kind'],event['summary'],event['description'],event['updated'],event['start'],event['end'],event['htmlLink'])
        sheet.update_cell(1,event['kind'])
        sheet.update_cell(2,event['description'])
        sheet.update_cell(3,event['updated'])
        sheet.update_cell(4,event['start'])
        sheet.update_cell(5,event['end'])
        sheet.update_cell(6,event['htmlLink'])   
        print("Events of Users:",events_u)
        print ("|")
        print ("|")
        print ("|")
      page_token = events.get('nextPageToken')
      if not page_token:
        break



if __name__ == '__main__':
    main()