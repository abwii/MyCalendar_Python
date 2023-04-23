# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.4 on Mon Mar 13 10:01:52 2023
#

from heapq import merge
import wx
from Ajout import Ajout
from Exporter import Exporter
from cal_setup import get_calendar_service
# begin wxGlade: dependencies
import wx.adv
# end wxGlade
import json
import os
# begin wxGlade: extracode
# end wxGlade


class MyCalendar(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyCalendar.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((600, 300))
        self.SetTitle("My Calendar")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(
            wx.Bitmap("img\gestionnaire_calendar.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.window_1 = wx.SplitterWindow(self.panel_1, wx.ID_ANY)
        self.window_1.SetMinimumPaneSize(20)
        sizer_1.Add(self.window_1, 1, wx.EXPAND, 0)

        self.window_1_pane_1 = wx.Panel(self.window_1, wx.ID_ANY)

        sizer_4 = wx.BoxSizer(wx.VERTICAL)

        label_1 = wx.StaticText(self.window_1_pane_1, wx.ID_ANY,
                                "Liste des topics", style=wx.ALIGN_CENTER_HORIZONTAL)
        label_1.SetMinSize((250, 30))
        label_1.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT,
                        wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_4.Add(label_1, 0, wx.ALL, 12)

        self.check_list_box_1 = wx.CheckListBox(self.window_1_pane_1, wx.ID_ANY, choices=[
                                                "Vacances (Zone A)", "Vacances (Zone B)", "Vacances (Zone C)", u"Jours Fériés", ""])
        sizer_4.Add(self.check_list_box_1, 0, wx.EXPAND | wx.SHAPED, 0)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(sizer_5, 1, wx.EXPAND, 0)

        self.btnGoogle = wx.Button(
            self.window_1_pane_1, wx.ID_ANY, u"Connexion à Google")
        sizer_5.Add(self.btnGoogle, 0, wx.ALIGN_CENTER_VERTICAL |
                    wx.EXPAND | wx.SHAPED, 0)

        imgGoogle = wx.StaticBitmap(self.window_1_pane_1, wx.ID_ANY, wx.Bitmap(
            "./img/F.png", wx.BITMAP_TYPE_ANY))
        sizer_5.Add(imgGoogle, 0, wx.ALIGN_CENTER_VERTICAL |
                    wx.EXPAND | wx.SHAPED, 0)

        self.checkbox_1 = wx.CheckBox(self.window_1_pane_1, wx.ID_ANY, "ZoneA")
        sizer_4.Add(self.checkbox_1, 0, 0, 0)

        self.checkbox_2 = wx.CheckBox(self.window_1_pane_1, wx.ID_ANY, "ZoneB")
        sizer_4.Add(self.checkbox_2, 0, 0, 0)

        self.checkbox_3 = wx.CheckBox(self.window_1_pane_1, wx.ID_ANY, "ZoneC")
        sizer_4.Add(self.checkbox_3, 0, 0, 0)

        self.btnMerge = wx.Button(self.window_1_pane_1, wx.ID_ANY, "button_1")
        sizer_4.Add(self.btnMerge, 0, 0, 0)

        self.print = wx.Button(self.window_1_pane_1, wx.ID_ANY, "button_1")
        sizer_4.Add(self.print, 0, 0, 0)

        self.window_1_pane_2 = wx.Panel(self.window_1, wx.ID_ANY)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)

        self.calendar = wx.adv.GenericCalendarCtrl(
            self.window_1_pane_2, wx.ID_ANY)
        sizer_2.Add(self.calendar, 0, wx.EXPAND, 0)

        sizer_3 = wx.GridSizer(1, 2, 0, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)

        self.btnAdd = wx.Button(self.window_1_pane_2, wx.ID_ANY, "Ajout ...")
        sizer_3.Add(self.btnAdd, 0, wx.EXPAND, 0)

        self.button_2 = wx.Button(self.window_1_pane_2, wx.ID_ANY, "Exporter")
        sizer_3.Add(self.button_2, 0, wx.EXPAND, 0)

        self.window_1_pane_2.SetSizer(sizer_2)

        self.window_1_pane_1.SetSizer(sizer_4)

        self.window_1.SplitVertically(
            self.window_1_pane_1, self.window_1_pane_2)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.ConnGoogle, self.btnGoogle)
        self.Bind(wx.EVT_CHECKBOX,
                  self.on_checkbox_topic_clicked, self.checkbox_1)
        self.Bind(wx.EVT_CHECKBOX,
                  self.on_checkbox_topic_clicked, self.checkbox_2)
        self.Bind(wx.EVT_CHECKBOX,
                  self.on_checkbox_topic_clicked, self.checkbox_3)
        self.Bind(wx.EVT_BUTTON, self.merge, self.btnMerge)
        self.Bind(wx.EVT_BUTTON, self.printer, self.print)
        self.Bind(wx.EVT_BUTTON, self.OnAdd, self.btnAdd)
        self.Bind(wx.EVT_BUTTON, self.OnExport, self.button_2)
        # end wxGlade
        # variable qui récupère les données du json
    checkbox1Content = ""
    checkbox2Content = ""
    checkbox3Content = ""
    mergedFile = ""

    def check1(self):
        print("start")
        if self.checkbox_1.GetValue():
            print("case cochée detectée")
            # La case à cocher est coché
            if not self.checkbox1Content:
                # vérifie si la variable est bien vide car si pleine, inutile de la re-remplir
                print("zone vide donc remplissage")
                # Code pour retourner un événement différent quand la case est cochée
                with open('json/checkbox/calendrier-scolaire-A.json', 'r') as f:
                    data1 = json.load(f)
                    self.checkbox1Content = data1
                    print("zone remplie avec succès, preuve:")
                    print(self.checkbox1Content)

            else:
                print("zone dejà remplie donc pass")
                print(self.checkbox1Content)

        else:
            print("case non cochée detectée")
            if self.checkbox1Content:
                print("zone remplie donc suppression")
                # vérifie si la variable est bien pleine car si vide, inutile de la re-vider
                self.checkbox1Content = ""
                print("zone retirée avec succès, preuve:")
                print(self.checkbox1Content)

            else:
                print("zone déjà vide donc pass")

    def check2(self):
        print("start")
        if self.checkbox_2.GetValue():
            print("case cochée detectée")
            # La case à cocher est coché
            if not self.checkbox2Content:
                # vérifie si la variable est bien vide car si pleine, inutile de la re-remplir
                print("zone vide donc remplissage")
                # Code pour retourner un événement différent quand la case est cochée
                with open('json/checkbox/calendrier-scolaire-B.json', 'r') as f:
                    data2 = json.load(f)
                    self.checkbox2Content = data2
                    print("zone remplie avec succès, preuve:")
                    print(self.checkbox2Content)

            else:
                print("zone dejà remplie donc pass")
                print(self.checkbox2Content)

        else:
            print("case non cochée detectée")
            if self.checkbox2Content:
                print("zone remplie donc suppression")
                # vérifie si la variable est bien pleine car si vide, inutile de la re-vider
                self.checkbox2Content = ""
                print("zone retirée avec succès, preuve:")
                print(self.checkbox2Content)

            else:
                print("zone déjà vide donc pass")

    def check3(self):
        print("start")
        if self.checkbox_3.GetValue():
            print("case cochée detectée")
            # La case à cocher est coché
            if not self.checkbox3Content:
                # vérifie si la variable est bien vide car si pleine, inutile de la re-remplir
                print("zone vide donc remplissage")
                # Code pour retourner un événement différent quand la case est cochée
                with open('json/checkbox/calendrier-scolaire-C.json', 'r') as f:
                    data3 = json.load(f)
                    self.checkbox3Content = data3
                    print("zone remplie avec succès, preuve:")
                    print(self.checkbox3Content)

            else:
                print("zone dejà remplie donc pass")
                print(self.checkbox3Content)

        else:
            print("case non cochée detectée")
            if self.checkbox3Content:
                print("zone remplie donc suppression")
                # vérifie si la variable est bien pleine car si vide, inutile de la re-vider
                self.checkbox3Content = ""
                print("zone retirée avec succès, preuve:")
                print(self.checkbox3Content)

            else:
                print("zone déjà vide donc pass")

    # wxGlade: MyCalendar.<event_handler>
    def on_checkbox_topic_clicked(self, event):
        self.check1()
        self.check2()
        self.check3()

    # def merge(folder_path, output_path, event):
    #     mergedFile = []
    #     folder_path = "json\checkbox"
    #     output_path = "json\checkbox\MergedFile.json"

    #     for filename in os.listdir(folder_path):
    #         if not filename.endswith(".json"):
    #             continue

    #         filepath = os.path.join(folder_path, filename)
    #         with open(filepath, "r") as f:
    #             data = json.load(f)
    #             mergedFile.extend(data)

    #     with open(output_path, "w") as f:
    #         json.dump(mergedFile, f)

    # def merge_files(self, event):  # wxGlade: MyCalendar.<event_handler>
    #     merge()
    #     print(self.mergedFile)
    # def merge(self):

        # # with open('json\checkbox\MergedFile.json', 'w') as f:
        # # merged_data = {**self.checkbox1Content, **self.checkbox2Content, **self.checkbox3Content}
        # # first = self.checkbox1Content.update(self.checkbox2Content)
        # # final = first.update(self.checkbox3Content)
        # # self.mergedFile = json.dump(merged_data, f)
        # content_list = [self.checkbox1Content,
        #                 self.checkbox2Content, self.checkbox3Content]
        # data_liste = []
        # for content in content_list:
        #     data = json.loads(content)
        #     data_liste += data
        # mergedFile = json.dumps(data_liste)

    def printer(self, event):
        print(self.mergedFile)

    def OnAdd(self, event):  # wxGlade: MyCalendar.<event_handler>
        addDialog = Ajout(self)
        result = addDialog.ShowModal()
        if(result == wx.ID_OK):
            self.lblReturn.SetLabelText(addDialog.txtEvt.GetValue())

    def ConnGoogle(self, event):  # wxGlade: MyCalendar.<event_handler>
        print("Connexion Google")
        get_calendar_service()
        # changement source image google connexion (👌)
        print("Fin Connexion Google")

    def OnExport(self, event):  # wxGlade: MyCalendar.<event_handler>
        addDialog = Exporter(self)
        result = addDialog.ShowModal()
        if(result == wx.ID_OK):
            self.lblReturn.SetLabelText(addDialog.txtEvt.GetValue())

    def merge(self, event):  # wxGlade: MyCalendar.<event_handler>
        # with open('json\checkbox', 'r') as f:
            # data_json = json.load(f)
            # data_json.update(self.checkbox1Content)
            # data_json.update(self.checkbox2Content)
            # data_json.update(self.checkbox3Content)
        mergedFile = []
        folder_path = "json\checkbox"
        output_path = "json\checkbox\MergedFile.json"

        for filename in os.listdir(folder_path):
            if not filename.endswith(".json"):
                continue

            filepath = os.path.join(folder_path, filename)
            with open(filepath, "r") as f:
                data = json.load(f)
                mergedFile.extend(data)

        with open(output_path, "w") as f:
            json.dump(mergedFile, f)

    with open('json\checkbox\MergedFile.json', 'w') as f:
            json.dump(mergedFile, f)
        # with open('json\checkbox\calendrier-scolaire-A.json', 'r') as f:
        #     data_json = json.load(f)


# end of class MyCalendar

# TODO BOUTON MERGE, à chaque clic sur un topic, avant de rechecker chaque json, une fonction viendra wipe le précédent json mergé
