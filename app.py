#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.4 on Sun Apr 23 16:03:15 2023
#

# This is an automatically generated file.
# Manual changes will be overwritten without warning!

import wx
from MyCalendar import MyCalendar


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyCalendar(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
