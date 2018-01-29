# -*- coding: utf-8 -*-

from wx_filedialog import *
from wx_table import *
from pandas_opendata import *
from wx_mpl_xy import *

class Open:
    def __init__(self):
        path = filedialog()
        que = Opendata(path.getpath())

        app = wx.App()

        #表の書き込み
        fr1 = TableFrame(None, que)
        fr1.fill_in(que)
        fr1.Show(True)

        #グラフ表示
        fr2 = wx.Frame(None, title='test')
        panel = XYPanel(fr2)
        panel.XYdraw(que)
        fr2.Show()

        app.MainLoop()