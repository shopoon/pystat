# -*- coding: utf-8 -*-
import pandas as pd
import numpy
import matplotlib as mpl
mpl.use('WXAgg')

import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

import wx

#日本語表示のためのフォント指定
mpl.rcParams["font.family"] = "AppleGothic"

class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

def selectMenu(event):
    if event.GetId() == 1:
        print("開けないよーん")
        #修正の必要あり、便宜的に今はsinカーブを表示
        frame_column = wx.Frame(frame, title = "column")
        panel_column = CanvasPanel(frame_column)
        t = numpy.arange(0.0, 3.0, 0.01)
        s = numpy.sin(2 * numpy.pi * t)
        panel_column.axes.plot(t, s)
        frame_column.Show()

def run():
    global frame
    application = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300,200))
    frame.CreateStatusBar()

    panel = wx.Panel(frame, wx.ID_ANY)
    panel.SetBackgroundColour("#AFAFAF")

    menu_file = wx.Menu()
    open_item = menu_file.Append(1, u"開く")
    save_item = menu_file.Append(2, u"保存")
    exit_item = menu_file.Append(3, u"終了")

    menu_edit = wx.Menu()
    copy_item  = menu_edit.Append(4, u"コピー")
    paste_item = menu_edit.Append(5, u"貼り付け")

    menu_bar = wx.MenuBar()
    menu_bar.Append(menu_file, u"ファイル")
    menu_bar.Append(menu_edit, u"編集")

    frame.Bind(wx.EVT_MENU,selectMenu)

    frame.SetMenuBar(menu_bar)

    frame.Show()
    application.MainLoop()

if __name__ == '__main__':
    run()
