import wx

import structure
import gui


rows = 18
cols = 12
number_of_bombs = 45

field = structure.get_field(rows, cols, number_of_bombs)

if __name__ == '__main__':
    app = wx.App()
    gui.Field(field, parent=None)
    app.MainLoop()
