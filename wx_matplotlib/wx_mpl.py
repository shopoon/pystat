# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

import wx

from wx_filedialog import *
from wx_table import *
from pandas_opendata import *


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

    def draw(self, data):
    # 課題：rangeの範囲やdata.table.ilocのrowの指定方法を考える
        x = []
        y = []
        for c in range(4):
            x.append(c+1)
            y.append(data.table.iloc[2, c])
        self.axes.plot(x, y)


if __name__ == "__main__":
    path = filedialog()
    que = Opendata(path.getpath())

    app = wx.App()

    frame = NewFrame(None)
    frame.fill_in(que)
    frame.Show(True)

    fr = wx.Frame(None, title='test')
    panel = CanvasPanel(fr)
    panel.draw(que)
    fr.Show()

    app.MainLoop()
