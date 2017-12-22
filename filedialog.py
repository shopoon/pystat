import wx

def selectData():
    app = wx.App()
    frame = wx.Frame(None, -1, 'win.py')
    frame.SetSize(0, 0, 200, 50)
    openFileDialog = wx.FileDialog(frame, "Open", "", "", "",
                                   wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

    openFileDialog.ShowModal()
    path = openFileDialog.GetPath()
    openFileDialog.Destroy()
    print(path + "からデータを読み込みました")
    return path

if __name__ == "__main__":
    selectData()