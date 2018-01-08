# -*- coding: utf-8 -*-

import wx


class filedialog:
    def getpath(self):
        app = wx.App()

        frame = wx.Frame(None, -1, 'win.py')
        frame.SetSize(0, 0, 200, 50)

        # Create open file dialog
        openFileDialog = wx.FileDialog(frame, "Open", "", "",
                                       "All files (*.*)|*.*",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openFileDialog.ShowModal()
        openFileDialog.Destroy()
        return openFileDialog.GetPath()


if __name__ == "__main__":
    test = filedialog()
    print(test.getpath())