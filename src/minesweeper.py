import wx

from menus import GeneralMenu
from minefield import MineField
from scoreboard import Scoreboard
from structure import FieldDataStructure


class Minesweeper(wx.Frame):
    rows = 10
    cols = 10
    number_of_bombs = 10

    def __init__(self, *args, **kwargs):
        super(Minesweeper, self).__init__(*args, **kwargs)

        self.menubar = GeneralMenu()
        scoreboard = Scoreboard(self)

        self.field_data = FieldDataStructure(self.rows, self.cols, self.number_of_bombs)
        minefield = MineField(self.field_data, parent=self)

        self.SetMenuBar(self.menubar)

        score_box = wx.BoxSizer(wx.VERTICAL)
        score_box.Add(scoreboard)

        self.minefield_box = wx.BoxSizer(wx.VERTICAL)
        self.minefield_box.Add(minefield)

        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(score_box)
        self.vbox.Add(self.minefield_box)
        self.SetSizerAndFit(self.vbox)
        self.Show()

    def restart_game(self):
        self.field_data.reset(self.rows, self.cols, self.number_of_bombs)
        new_minefield = MineField(self.field_data, parent=self)

        old_minefield = self.minefield_box.GetItem(0).GetWindow()

        self.minefield_box.Replace(old_minefield, new_minefield)
        self.minefield_box.Layout()

        old_minefield.Destroy()


if __name__ == '__main__':
    app = wx.App()
    Minesweeper(None, title="Minesweeper")
    app.MainLoop()
