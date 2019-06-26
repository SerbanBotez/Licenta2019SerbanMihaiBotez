import wx

# MAIN PROGRAM...
class MyFrame(wx.Frame):

    def __init__(self):

     wx.Frame.__init__(self, None, -1, "My Frame", size = (600, 600))

     mainPanel = wx.Panel(self)
     mainBox = wx.BoxSizer(wx.VERTICAL)

     header1 = wx.StaticText(mainPanel, label = 'Header1:')
     header2 = wx.StaticText(mainPanel, label = 'Header2:')

     panel1 = wx.Panel(mainPanel, size = (200, 200), style = wx.SUNKEN_BORDER)
     panel2 = wx.Panel(mainPanel, size = (200, 200), style = wx.SUNKEN_BORDER)

     box1 = wx.BoxSizer(wx.HORIZONTAL)
     box1.AddSpacer(50)
     box1.Add(header1, 0, wx.ALL, 5)
     box1.AddSpacer(50)
     box1.Add(header2, 0, wx.ALL, 5)

     box2 = wx.BoxSizer(wx.HORIZONTAL)
     box2.Add(panel1, 0, wx.ALL, 5)
     box2.Add(panel2, 0, wx.ALL, 5)

     mainBox.Add(box1, 0, wx.ALL, 5)
     mainBox.Add(box2, 0, wx.ALL, 5)

     mainPanel.SetSizer(mainBox)
     #self.Center()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()

    print('Exiting...')