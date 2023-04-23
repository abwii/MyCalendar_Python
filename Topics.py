import json

zoneA =""
zoneB =""
zoneC =""

def check(self, zone):
            if self.zone.GetValue():
                # La case à cocher est cochée
                if not zone:
                    #vérifie si la variable est bien vide car si pleine, inutile de la re-remplir
                    print("Deadmau5 connected to zone")
                    # Code pour retourner un événement différent quand la case est cochée
                    with open('MyCalendar_Python-main/json/topics/zoneA.json', 'r') as f:
                        data = json.load(f)
                        zone = data
                        print(zone)
                else:
                    pass

            else:
                if zone:
                    #vérifie si la variable est bien pleine car si vide, inutile de la re-vider
                    print("Deadmau5 disconnected from zone")
                    zone = ""
                    print("zone retirée avec succès")
                else:
                    pass




def on_checkbox_topic_clicked(self, event):  # wxGlade: MyCalendar.<event_handler>
    check(zoneA)
    check(zoneB)
    check(zoneC)
      
            
            
        