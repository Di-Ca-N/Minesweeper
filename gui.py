import wx


class Field(wx.Frame):
    button_size = 40

    def __init__(self, field, *args, **kwargs):
        super(Field, self).__init__(*args, **kwargs)

        self.width = len(field[0]) * self.button_size
        self.row_length = len(field[0])
        self.col_length = len(field)

        self.alive = True

        vbox = wx.BoxSizer(wx.VERTICAL)

        header = self.generate_header()
        vbox.Add(header, flag=wx.CENTER)

        matrix = self.generate_field(field)
        vbox.Add(matrix, flag=wx.CENTER)

        self.SetSizerAndFit(vbox)
        self.SetBackgroundColour(wx.LIGHT_GREY)
        # self.SetSize(self.width, self.width+header.GetSize()[1],)
        self.Show()

    def generate_field(self, field):
        rows = len(field)
        cols = len(field[0])

        vbox = wx.BoxSizer(wx.VERTICAL)

        for row in range(rows):
            hbox = wx.BoxSizer(wx.HORIZONTAL)
            for col in range(cols):
                button = wx.Button(self, id=wx.NewId(), size=(self.button_size, self.button_size))

                button.state = 'closed'
                button.value = field[row][col]
                button.position = (row, col)

                button.SetBackgroundColour(wx.LIGHT_GREY)

                button.Bind(wx.EVT_RIGHT_DOWN, self.on_button_right_click)
                button.Bind(wx.EVT_LEFT_DOWN, self.on_button_click)

                hbox.Add(button, flag=wx.CENTER)
            vbox.Add(hbox, flag=wx.CENTER)

        return vbox

    def generate_header(self):
        panel = wx.Panel(self)

        wx.StaticText(panel, label="Campo Minado", style=wx.ALIGN_CENTER)

        return panel

    def on_button_right_click(self, event):
        clicked_button = event.GetEventObject()
        if clicked_button.state == 'closed':
            clicked_button.state = 'marked'
            clicked_button.SetBackgroundColour(wx.RED)

        elif clicked_button.state == 'marked':
            clicked_button.SetBackgroundColour(wx.LIGHT_GREY)


    def on_button_click(self, event):
        clicked_button = event.GetEventObject()
        if self.alive:
            self.propagate_click(clicked_button.GetId())

    def propagate_click(self, button_id):
        button = self.FindWindowById(button_id)
        button.SetBackgroundColour(wx.YELLOW)

        button.state = 'opened'

        if button.value == '0':
            list(map(self.propagate_click, self.get_neighbors(button)))

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

            valid_id = 100 <= neighbor_id < (self.row_length * self.col_length) + 100
            really_neighbor = False
            valid_state = False

            if valid_id:
                really_x_neighbor = neighbor_button.position[0] in (button.position[0] - 1,
                                                                    button.position[0],
                                                                    button.position[0] + 1)

                really_y_neighbor = neighbor_button.position[1] in (button.position[1] - 1,
                                                                    button.position[1],
                                                                    button.position[1] + 1)

                really_neighbor = really_x_neighbor and really_y_neighbor

                valid_state = neighbor_button.state == 'closed'

            if valid_id and really_neighbor and valid_state:
                true_neighbors.append(neighbor_id)

        return true_neighbors

    @staticmethod
    def resize_image_to_button_size(path_to_image, width, height):
        bitmap = wx.Bitmap(path_to_image)
        resized_image = bitmap.ConvertToImage().Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        return resized_image

    def game_over(self):
        self.alive = False
        wx.MessageBox("Game Over")
