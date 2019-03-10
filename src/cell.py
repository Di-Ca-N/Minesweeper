import wx


class Cell(wx.Button):
    def __init__(self, value, position, state='closed', *args, **kwargs):
        super(Cell, self).__init__(*args, **kwargs)
        self.value = value
        self.position = position
        self.state = state

        self.SetBackgroundColour(wx.LIGHT_GREY)

    def open(self):
        if self.value != '0':
            self.SetLabel(self.value)

        if self.value == '*':
            self.SetBackgroundColour(wx.RED)
        else:
            self.SetBackgroundColour(wx.YELLOW)

        self.state = 'opened'
        return self.value

    def mark(self):
        self.SetBackgroundColour(wx.RED)
        self.state = 'marked'
