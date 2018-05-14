# -*- coding: utf-8 -*-

from wx_filedialog import *
from wx_table import *
from pandas_opendata import *
from wx_mpl_xy import *
from wx_mpl_column import *

class Open:
    def __init__(self):
        self.__que = Opendata(filedialog.getpath())

    def show(self):
        #表の書き込み
        #グラフ毎に表の設定も変えることになるのなら、変更必要かも
        #app = wx.App() は継承後のクラスに毎回入れないとなぜかエラー出る
        fr1 = TableFrame(None, self.que)
        fr1.fill_in(self.que)
        fr1.Show()

    @property
    def que(self):
        return self.__que

class Open_xy(Open):
    def __init__(self):
        self.__que = Opendata_xy(filedialog.getpath())

    def show(self):
        app = wx.App()
        super().show()
        #xyグラフ表示
        fr2 = wx.Frame(None, title='test')
        panel = XYPanel(fr2)
        panel.XYdraw(self.que)
        fr2.Show()

        app.MainLoop()

    @property
    def que(self):
        return self.__que

class Open_bar(Open):
    def __init__(self):
        self.__que = Opendata_bar(filedialog.getpath())

    def show(self):
        app = wx.App()
        super().show()

        #棒グラフ表示
        fr2 = wx.Frame(None, title='test')
        panel = BarPanel(fr2)
        panel.bar_draw(self.que)
        fr2.Show()

        app.MainLoop()

    @property
    def que(self):
        return self.__que
