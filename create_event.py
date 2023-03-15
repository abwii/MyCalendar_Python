import os.path
import json
from os import path
from datetime import datetime, timedelta
from cal_setup import get_calendar_service


def create_event(idCalendar):

   print ("ID de l'agenda : ", idCalendar)

   service = get_calendar_service()

   with open('nomDuJsonCompilé.json', 'r') as f:
      data = json.load(f)
      print(len(data))



   for i in range (0, len(data)) :

      if data[i]['end'] == None : #si le json ne contient pas une date de fin -> d = date du début + 1 jour
         a = data[i]['summary']
         b = data[i]['description']
         c = data[i]['start']
         d = data[i]['start' + 1]
      
      else : #si le json contient une date de fin -> d = date de fin
         a = data[i]['summary']
         b = data[i]['description']
         c = data[i]['start']
         d = data[i]['end']

      event_result = service.events().insert(
         calendarId=idCalendar,
         body={
            "summary": a,
            "description": b,
            "start": {"dateTime": c, "timeZone": 'UTC+1'},
            "end": {"dateTime": d, "timeZone": 'UTC+1'},
         }
      )

   event_result.execute()

   print("Succès")