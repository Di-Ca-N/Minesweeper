import wx

from structure import FieldDataStructure
import gui


rows = 10
cols = 10
number_of_bombs = 10

data_structure = FieldDataStructure(rows, cols, number_of_bombs)

if __name__ == '__main__':
    app = wx.App()
    gui.MineField(data_structure, parent=None)
    app.MainLoop()
