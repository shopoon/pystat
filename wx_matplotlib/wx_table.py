# -*- coding: utf-8 -*-

import wx
import wx.grid

from wx_filedialog import *
from pandas_opendata import *


class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent, colNo = 20, rowNo = 20):
        wx.grid.Grid.__init__(self, parent, -1)
        self.CreateGrid(colNo, rowNo)


class TableFrame(wx.Frame):
    def __init__(self, parent, data):
        wx.Frame.__init__(self, parent, -1, "New Table", size=(800, 400))
        self.new_table = SimpleGrid(self, len(data.table.index), len(data.table.columns))
    def fill_in(self, data):
        for i in range(len(data.table.index)): #表の枠外の行ラベルを自然数に設定
            self.new_table.SetRowLabelValue(i, str(i+1))
        for r in range(len(data.table.index)):
            for c in range(len(data.table.columns)): #表にデータを書き込み
                val = data.table.iloc[r, c]
                self.new_table.SetCellValue(r, c, str(val))


if __name__ == "__main__":
    path = filedialog()
    que = Opendata(path.getpath())
    app = wx.App()
    frame = TableFrame(None)
    frame.fill_in(que)
    frame.Show(True)
    app.MainLoop()
