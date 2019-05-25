import wx

from cell import Cell


class MineField(wx.Panel):
    def __init__(self, field_data, *args, **kwargs):
        super(MineField, self).__init__(*args, **kwargs)

        self.field_data = field_data

        self.field = self.generate_field()
        self.alive = True

        self.SetSizerAndFit(self.field)

        self.SetBackgroundColour(wx.BLACK)
        self.Show()

    def generate_field(self):
        sizer = wx.GridBagSizer(1, 1)

        for row in range(self.field_data.rows):
            for col in range(self.field_data.cols):
                cell = Cell(value=self.field_data[row][col], position=(row, col), parent=self)
                cell.Bind(wx.EVT_LEFT_DOWN, self.on_cell_click)
                cell.Bind(wx.EVT_RIGHT_DOWN, self.on_cell_right_click)
                sizer.Add(cell, pos=wx.GBPosition(*cell.position))

        return sizer

    def on_cell_click(self, event):
        clicked_cell = event.GetEventObject()

        if self.alive:
            if clicked_cell.is_closed():
                self.propagate_click(clicked_cell)

            elif clicked_cell.is_open():
                number_of_marked_neighbors = self.count_marked_neighbors(clicked_cell)

                if number_of_marked_neighbors == int(clicked_cell.value):
                    neighbors = clicked_cell.get_neighbor_positions(self.field_data.rows, self.field_data.cols)

                    for neighbors_pos in neighbors:
                        neighbor_cell = self.field.FindItemAtPosition(wx.GBPosition(*neighbors_pos)).GetWindow()
                        self.propagate_click(neighbor_cell)

            if self.verify_victory():
                self.set_win()

    def on_cell_right_click(self, event):
        clicked_cell = event.GetEventObject()
        if self.alive:
            clicked_cell.toggle_mark()

            if self.verify_victory():
                self.set_win()

    def count_marked_neighbors(self, cell):
        neighbors = cell.get_neighbor_positions(self.field_data.rows, self.field_data.cols)

        marked_neighbors = 0
        for neighbor_position in neighbors:
            cell = self.field.FindItemAtPosition(wx.GBPosition(*neighbor_position)).GetWindow()
            if cell.is_marked():
                marked_neighbors += 1

        return marked_neighbors

    def propagate_click(self, cell):
        if cell.is_closed():
            value = cell.open()

            if value == '0':
                for each_neighbor in cell.get_neighbor_positions(self.field_data.rows, self.field_data.cols):
                    neighbor_cell = self.field.FindItemAtPosition(wx.GBPosition(*each_neighbor)).GetWindow()
                    self.propagate_click(neighbor_cell)

            elif value == '*':
                self.set_game_over()

    def verify_victory(self):
        marked_bombs = 0
        only_bombs_marked = True
        total_bombs = len(self.field_data.bombs_places)

        for row in range(self.field_data.rows):
            for col in range(self.field_data.cols):

                cell = self.field.FindItemAtPosition(wx.GBPosition(row, col)).GetWindow()
                if cell.is_marked():
                    if cell.value == '*':
                        marked_bombs += 1
                    else:
                        only_bombs_marked = False

        if marked_bombs == total_bombs and only_bombs_marked:
            return True

        return False

    def set_game_over(self):
        if self.alive:
            self.alive = False
            wx.MessageBox("Game Over!")

    def set_win(self):
        wx.MessageBox("You Win!")
        self.alive = False
