# -*- coding: utf-8 -*-
import wx
from event_handler import *

def selectMenu(event):
    if event.GetId() == 11:
        select = Open_xy()
    elif event.GetId() == 12:
        select = Open_bar()

    select.show()



application = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300,200))
frame.CreateStatusBar()

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

menu_file = wx.Menu()

open_item = wx.Menu()
open_xy = open_item.Append(11, u"XYグラフ")
open_bar = open_item.Append(12, u"棒グラフ")
menu_file.AppendSubMenu(open_item,u"新規作成")

save_item = menu_file.Append(2, u"保存")
exit_item = menu_file.Append(1, u"終了")

menu_edit = wx.Menu()
copy_item  = menu_edit.Append(3, u"コピー")
paste_item = menu_edit.Append(4, u"貼り付け")

menu_bar = wx.MenuBar()
menu_bar.Append(menu_file, u"ファイル")
menu_bar.Append(menu_edit, u"編集")

frame.Bind(wx.EVT_MENU,selectMenu)

frame.SetMenuBar(menu_bar)

frame.Show()
application.MainLoop()
