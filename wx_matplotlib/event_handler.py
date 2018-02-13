# -*- coding: utf-8 -*-

from wx_filedialog import *
from wx_table import *
from pandas_opendata import *
from wx_mpl_xy import *
from wx_mpl_column import *

class Open:
    def __init__(self):
        self.__path = filedialog()
        self.__que = Opendata(self.__path.getpath())
    def show(self):
        return

    @property
    def que(self):
        return self.__que

class Open_xy(Open):
    def show(self):
        app = wx.App()

        #表の書き込み
        #[課題] 表とグラフは別クラスすべきかもしれない
        fr1 = TableFrame(None, self.que)
        fr1.fill_in(self.que)
        fr1.Show()

        #xyグラフ表示
        fr2 = wx.Frame(None, title='test')
        panel = XYPanel(fr2)
        panel.XYdraw(self.que)
        fr2.Show()

        app.MainLoop()

class Open_bar(Open):
    def show(self):
        app = wx.App()

        #表の書き込み
        #[課題] 表とグラフは別クラスすべきかもしれない
        fr1 = TableFrame(None, self.que)
        fr1.fill_in(self.que)
        fr1.Show()

        #棒グラフ表示
        fr2 = wx.Frame(None, title='test')
        panel = BarPanel(fr2)
        panel.bar_draw(self.que)
        fr2.Show()

        app.MainLoop()
