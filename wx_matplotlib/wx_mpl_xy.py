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
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)

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

    frame = TableFrame(None)
    frame.fill_in(que)
    frame.Show(True)

    fr = wx.Frame(None, title='test')
    panel = XYPanel(fr)
    panel.draw(que)
    fr.Show()

    app.MainLoop()
