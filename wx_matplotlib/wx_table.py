# -*- coding: utf-8 -*-

import wx
import wx.grid

from wx_filedialog import *
from pandas_opendata import *


class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent, colNo, rowNo):
        wx.grid.Grid.__init__(self, parent, -1)
        self.CreateGrid(colNo, rowNo)


class TableFrame(wx.Frame):
    def __init__(self, parent, col_no = 20, row_no = 20):
        wx.Frame.__init__(self, parent, -1, "New Table", size=(800, 400))
        self.new_table = SimpleGrid(self, col_no, row_no)
    def fill_in(self, data):
        """
        rangeの範囲の指定方法を考える。
        データの大きさを読み取って、
        必要ならばtableの大きさを変えるようにしないといけない。
        """
        for i in range(3):
            self.new_table.SetRowLabelValue(i, str(i+1))
        for r in range(3):
            for c in range(4):
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
