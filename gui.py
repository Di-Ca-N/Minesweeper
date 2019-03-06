import wx


class MineField(wx.Frame):
    button_size = 35

    def __init__(self, field_data_structure, *args, **kwargs):
        super(MineField, self).__init__(*args, **kwargs)

        self.width = field_data_structure.cols * self.button_size
        self.row_length = field_data_structure.rows
        self.col_length = field_data_structure.cols
        self.bomb_positions = field_data_structure.bomb_places

        self.alive = True

        vbox = wx.BoxSizer(wx.VERTICAL)

        header = self.generate_header()
        vbox.Add(header, flag=wx.CENTER)

        matrix = self.generate_field(field_data_structure)
        vbox.Add(matrix, flag=wx.CENTER)

        self.SetSizerAndFit(vbox)
        self.SetBackgroundColour(wx.BLACK)
        self.Show()

    def generate_field(self, field_data_structure):
        rows = field_data_structure.rows
        cols = field_data_structure.cols

        sizer = wx.GridSizer(self.row_length, self.col_length, 1, 1)

        for row in range(rows):
            for col in range(cols):
                button = wx.Button(self, id=wx.NewId(), size=(self.button_size, self.button_size), style=wx.NO_BORDER)

                button.state = 'closed'
                button.value = field_data_structure[row][col]
                button.position = (row, col)

                button.SetBackgroundColour(wx.LIGHT_GREY)

                button.Bind(wx.EVT_RIGHT_DOWN, self.on_button_right_click)
                button.Bind(wx.EVT_LEFT_DOWN, self.on_button_click)

                sizer.Add(button)

        return sizer

    def generate_header(self):
        panel = wx.Panel(self)

        text = wx.StaticText(panel, label="Campo Minado", style=wx.ALIGN_CENTER)
        text.SetForegroundColour(wx.WHITE)
        font = wx.Font('Arial')
        font.SetPointSize(16)
        text.SetFont(font)

        return panel

    def on_button_right_click(self, event):
        clicked_button = event.GetEventObject()
        if self.alive:
            if clicked_button.state == 'closed':
                clicked_button.state = 'marked'
                clicked_button.SetBackgroundColour(wx.RED)

            elif clicked_button.state == 'marked':
                clicked_button.state = 'closed'
                clicked_button.SetBackgroundColour(wx.LIGHT_GREY)

            if self.verify_victory():
                self.win()

    def on_button_click(self, event):
        clicked_button = event.GetEventObject()
        if self.alive:
            if clicked_button.state == 'closed':
                self.propagate_click(clicked_button.GetId())

            elif clicked_button.state == 'opened':
                neighbors = self.get_neighbors(clicked_button)
                marked_neighbors = 0
                for each_neighbor in neighbors:
                    button = wx.FindWindowById(each_neighbor)
                    if button.state == 'marked':
                        marked_neighbors += 1

                if marked_neighbors == int(clicked_button.value):
                    for each_neighbor in neighbors:
                        self.propagate_click(each_neighbor)

            if self.verify_victory():
                self.win()

    def propagate_click(self, button_id):
        button = self.FindWindowById(button_id)
        if button.state == 'closed':
            button.SetBackgroundColour(wx.YELLOW)

            button.state = 'opened'

            if button.value == '0':
                for each_neighbor in self.get_neighbors(button):
                    self.propagate_click(each_neighbor)

            else:
                button.SetLabel(button.value)

                if button.value == '*':
                    button.SetBackgroundColour(wx.RED)
                    self.game_over()

    def get_neighbors(self, button):
        button_id = button.GetId()

        all_neighbors = [
            button_id-self.row_length-1, button_id-self.row_length, button_id-self.row_length+1,
            button_id-1,                                            button_id+1,
            button_id+self.row_length-1, button_id+self.row_length, button_id+self.row_length+1,
        ]

        true_neighbors = []

        for neighbor_id in all_neighbors:
            neighbor_button = self.FindWindowById(neighbor_id)

            valid_id = 100 <= neighbor_id < self.get_max_id()
            really_neighbor = False

            if valid_id:
                really_x_neighbor = neighbor_button.position[0] in (button.position[0] - 1,
                                                                    button.position[0],
                                                                    button.position[0] + 1)

                really_y_neighbor = neighbor_button.position[1] in (button.position[1] - 1,
                                                                    button.position[1],
                                                                    button.position[1] + 1)

                really_neighbor = really_x_neighbor and really_y_neighbor

            if valid_id and really_neighbor:
                true_neighbors.append(neighbor_id)

        return true_neighbors

    @staticmethod
    def resize_image_to_button_size(path_to_image, width, height):
        bitmap = wx.Bitmap(path_to_image)
        resized_image = bitmap.ConvertToImage().Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        return resized_image

    def verify_victory(self):
        marked_bombs = 0
        only_bombs_marked = True
        total_bombs = len(self.bomb_positions)
        print('começou')
        for cell_id in range(100, self.get_max_id()):
            cell = wx.FindWindowById(cell_id)
            if cell.state == 'marked':
                if cell.value == '*':
                    marked_bombs += 1
                else:
                    only_bombs_marked = False

        print('terminou')
        if marked_bombs == total_bombs and only_bombs_marked:
            return True

        return False


    def get_max_id(self):
        return self.col_length * self.row_length + 100

    def game_over(self):
        if self.alive:
            self.alive = False
            wx.MessageBox("Game Over!")

    def win(self):
        wx.MessageBox("You Win!")
