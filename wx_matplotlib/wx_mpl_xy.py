# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import Toolbar, FigureCanvasWxAgg as FigureCanvas
#from matplotlib.backends.backend_wx import Toolbar
from matplotlib.figure import Figure

import wx

from wx_filedialog import *
from wx_table import *
from pandas_opendata import *


class XYPanel(wx.Panel):
    def __init__(self, parent):
        self.parent = parent
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        # self.figure.set_facecolor(0.9,0.9,1.0)
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        # self.canvas.SetBackgroundColour(wx.Colour(100, 255, 255))

        """
        以下の#self.~のコメントを外すとmatplotlibのtoolbarを使えるが、
        matplotlibのwx_compat.pyを書き変える必要がある
        """

        #self.toolbar = Toolbar(self.canvas)  # matplotlib toolbar
        #self.toolbar.Realize() #self.toolbar.set_active([0,1])を足しても良い？
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        # Best to allow the toolbar to resize!
        #self.sizer.Add(self.toolbar, 0, wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

    def XYdraw(self, data):
        x = []
        y = []
        for i in range(len(data.table.index)):
            x_temp = []
            y_temp = []
            for c in range(len(data.table.columns)):
                if c == 0:
                    continue
                x_temp.append(data.table.iloc[i, 0])
                y_temp.append(data.table.iloc[i, c])
                x.append(x_temp)
                y.append(y_temp)
            self.axes.plot(x, y)


if __name__ == "__main__":
    path = filedialog()
    que = Opendata(path.getpath())

    app = wx.App()

    frame = TableFrame(None)
    frame.fill_in(que)
    frame.Show(True)

    fr = wx.Frame(None, title='test')
    panel = XYPanel(fr)
    panel.XYdraw(que)
    fr.Show()

    app.MainLoop()
