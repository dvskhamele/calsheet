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

import time 

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
                        0)

    name = 'you'
    nominee = 'nominee_name'
    relation = 'relation'

    from oauth2client import file, client, tools
    store = file.Storage('sync/token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)

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
    ids=sheet.col_values(21)
    row=sheet.row_values(6)
    row_to_update = len(ids)+1



    for calendarId in [calendarId_record, calendarId_surgeries, calendarId_important ]:
      eventss = service.events().list(calendarId=calendarId, pageToken=page_token).execute()
      for key, value in eventss.items():
        try:
          for key, value in value.items():
           
                        print(key,value)
                        print()
                        events_u=events['description'],events['htmlLink']
        except:
            pass                                                                               
                                                                                                

      for event in eventss['items']:
        if event['id'] not in ids:
          row_to_update = row_to_update +1
          time.sleep(1)
          if calendarId==calendarId_surgeries:
            sheet.update_cell(row_to_update, 16, 'no')
            sheet.update_cell(row_to_update, 19, 'Democalender')

          if calendarId==calendarId_important:
            sheet.update_cell(row_to_update, 16, 'no')
            sheet.update_cell(row_to_update, 19, 'Important')
          if calendarId==calendarId_record:
            sheet.update_cell(row_to_update, 16, 'yes')
            sheet.update_cell(row_to_update, 19, 'Records')
          sheet.update_cell(row_to_update, 21, event['id'])
          time.sleep(1)
          date_s = str(event['start'])
          ab=str(date_s[14:24])                   
          bc= str(date_s[26:39])
          try:
            loct = str(event['location'])
            sheet.update_cell(row_to_update, 10, loct)
            print(loct)
          except:
            pass
          sheet.update_cell(row_to_update, 16, str(event['reminders']["overrides"][0]["method"]))
          sheet.update_cell(row_to_update, 11, ab)
          sheet.update_cell(row_to_update, 13, bc)

          date_e = str(event['end'])
          print (date_e)
          de=str(date_s[14:24])                   
          sheet.update_cell(row_to_update, 12, de)
          ef= str(date_s[26:39])
          time.sleep(1)  
          sheet.update_cell(row_to_update, 14, ef)
          des = str(event['description']).split("\n")          
          print("Updating", event["id"])
          a= str(des[1])
          sheet.update_cell(row_to_update,1, a[10:])
          b= str(des[2])
          sheet.update_cell(row_to_update,2, b[8:])
          time.sleep(1)  
          c= str(des[3])
          sheet.update_cell(row_to_update,3, c[9:])
          d= str(des[4])          
          sheet.update_cell(row_to_update,4, d[5:])
          e= str(des[5])
          time.sleep(1)  
          sheet.update_cell(row_to_update,6, e[24:])
          f= str(des[6])
          sheet.update_cell(row_to_update,7, f[12:])
          sheet.update_cell(row_to_update, 20, event['htmlLink'])
        else:
                    print("already Updating", event["id"])



if __name__ == '__main__':
    main()