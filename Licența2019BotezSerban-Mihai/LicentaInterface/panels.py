import wx
import wx.lib.scrolledpanel

def click(event):
    global text
    wx.MessageBox(text.Value)


app = wx.App()

frame = wx.Frame(None,size =(800, 400))
panel2 = wx.lib.scrolledpanel.ScrolledPanel(frame, -1, pos=(0, 28), style=wx.SIMPLE_BORDER)
#panel.SetBackgroundColour('#FDDF99')
panel2.SetupScrolling()

box = wx.BoxSizer(wx.VERTICAL)

t = 'dada'

text = wx.StaticText(panel2, label=t)

output = wx.TextCtrl(panel2)

box.Add(text, 0, wx.RIGHT, 5)
box.Add(output, 0, wx.RIGHT, 5)

panel2.SetSizer(box)
panel2.Layout()

"""

bSizer = wx.BoxSizer(wx.VERTICAL)
bSizer.Add(text, 0, wx.ALL, 5)
i = 0




while i < 10000:
        t = t + 'a'
        text = wx.StaticText(panel2, label=t)
        bSizer.Add(text, 0, wx.ALL, 5)
        i = i + 1
        panel2.SetSizer(bSizer)

"""



frame.Show()
app.MainLoop()