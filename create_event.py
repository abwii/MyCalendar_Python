import os.path
import json
from os import path
from datetime import datetime, timedelta
from cal_setup import get_calendar_service


def create_event(idCalendar):

   print ("ID de l'agenda : ", idCalendar)

   service = get_calendar_service()

   with open('json\mergedJson.json', 'r') as f:
      data = json.load(f)
      print(len(data))

      my_dico = json.dumps(data)

      for t in range (0,len(data)) :
         data_washed = my_dico.replace('], [', '').replace('],[', '').replace('] ,[', '').replace('] , [', '').replace('}{', '},{').replace('[[', '[').replace(']]', ']').replace('}]{', '}{')
         data_rinced = data_washed.replace('[[', '[').replace(']]', ']').replace('}{','},{')

      print ("rinced = ", data_rinced)

      data_cleaned = json.loads(data_rinced)

      print ("my dico = ", data_cleaned)






   for i in range (0, len(data_cleaned)) :

      if data_cleaned[i]['end'] == "" : #si le json ne contient pas une date de fin -> d = date du début + 1 jour
         print ("NON pas de date")
         a = data_cleaned[i]['summary']
         b = data_cleaned[i]['description']
         c = data_cleaned[i]['start']
         d = c
         
      
      else : #si le json contient une date de fin -> d = date de fin
         print ("OUI date")
         a = data_cleaned[i]['summary']
         b = data_cleaned[i]['description']
         c = data_cleaned[i]['start']
         d = data_cleaned[i]['end']

      print("|a = ",a,"|b = ",b,"|c = ",c,"|d = ",d)

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