import wx


class Scoreboard(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(Scoreboard, self).__init__(*args, **kwargs)
        vbox = wx.BoxSizer(wx.VERTICAL)

        header = self.generate_header()
        vbox.Add(header)

        self.SetSizer(vbox)
        self.SetBackgroundColour(wx.BLACK)
        self.Show()

    def generate_header(self):
        text = wx.StaticText(self, label="Campo Minado", style=wx.ALIGN_CENTER)
        text.SetForegroundColour(wx.WHITE)
        font = wx.Font(wx.FONTSIZE_LARGE, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        font.SetPointSize(20)
        text.SetFont(font)

        return text

