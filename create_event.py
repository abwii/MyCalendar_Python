import os.path
import json
from os import path
from datetime import datetime, timedelta
from cal_setup import get_calendar_service


def create_event(idCalendar):

   print ("ID de l'agenda : ", idCalendar)

   service = get_calendar_service()

   with open('json\checkbox\MergedFile.json', 'r') as f:
      data = json.load(f)
      print(len(data), "événements à ajouter")



   for i in range (0, len(data)) :

      if data[i]['end'] == None : #si le json ne contient pas une date de fin -> d = date du début + 1 jour
         a = data[i]['summary']
         b = data[i]['start' + 1]
         c = data[i]['start']
         d = data[i]['description']
      
      else : #si le json contient une date de fin -> d = date de fin
         a = data[i]['summary']
         b = data[i]['start']
         c = data[i]['end']
         d = data[i]['description']

      event_result = service.events().insert(
         calendarId=idCalendar,
         body={
            "summary": a,
            "start": {"dateTime": b, "timeZone": 'UTC+1'},
            "end": {"dateTime": c, "timeZone": 'UTC+1'},
            "description": d,
         }
      )

   event_result.execute()

   print("Succès")