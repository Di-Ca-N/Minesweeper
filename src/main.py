import wx

from .structure import FieldDataStructure
from .minefield import MineField


rows = 15
cols = 17
number_of_bombs = 30

if __name__ == '__main__':
    app = wx.App()
    data_structure = FieldDataStructure(rows, cols, number_of_bombs)
    MineField(data_structure, parent=None)
    app.MainLoop()
