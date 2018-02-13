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

#日本語表示のためのフォント指定
matplotlib.rcParams["font.family"] = "MS Gothic"

class BarPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(1,1,1)
        self.canvas = FigureCanvas(self, -1, self.figure)
        #self.toolbar = Toolbar(self.canvas)  # matplotlib toolbar
        #self.toolbar.Realize()
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.axes.set_frame_on(False)
        self.axes.set_axis_on()
        self.SetSizer(self.sizer)
        self.Fit()

    def bar_draw(self, data):
        self.data_statistics = data.table.describe()
        self.x = data.table.columns
        self.y_mean = self.data_statistics.loc["mean", self.x]

        self.axes.bar(range(len(self.x)),
                      self.y_mean,
                      yerr=self.data_statistics.loc["std", self.x],
                      ecolor="black", capsize=5, #エラーバーの設定
                      tick_label=self.x,
                      linewidth = 1, edgecolor = "#000000", zorder = 1)
        """
        課題：
        1.
        header = Noneでcsvファイルを開いている
        （pandas_opendata.pyのOpendataのself.tableにて）
        そのため、棒グラフの名前を取得する方法が無い。
        グラフ毎にopenfileクラスを作るしかない？

        2.
        カラムの色を1本ずつ変えたい

        3.
        エラーバーをSEMにする、片側だけ表示にする
        """


if __name__ == "__main__":
    path = filedialog()
    que = Opendata(path.getpath())

    app = wx.App()

    frame = TableFrame(None,que)
    frame.fill_in(que)
    frame.Show(True)

    fr = wx.Frame(None, title='test')
    panel = XYPanel(fr)
    panel.draw(que)
    fr.Show()

    app.MainLoop()
