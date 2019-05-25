import wx
import images


MARKED = 'marked'
CLOSED = 'closed'
OPENED = 'opened'
DEFAULT_KWARGS = {'style': wx.NO_BORDER, 'size': (32, 32)}


class Cell(wx.Button):
    def __init__(self, value, position, state=CLOSED, *args, **kwargs):
        kwargs = dict(DEFAULT_KWARGS, **kwargs)  # Dict Union
        super().__init__(*args, **kwargs)

        self.value = value
        self.position = position
        self.state = state

        self.images = images.get_images(self.GetSize())
        self.SetBackgroundColour(wx.LIGHT_GREY)

    def __repr__(self):
        return "Cell(value={}, position={}, state={})".format(self.value, self.position, self.state)

    def open(self):
        if self.value != '0':
            self.SetLabel(self.value)

        if self.value == '*':
            self.SetBackgroundColour(wx.RED)
            self.SetBitmap(self.images['BOMB'])
        else:
            self.SetBackgroundColour(wx.YELLOW)

        self.state = OPENED
        return self.value

    def toggle_mark(self):
        if self.is_closed():
            self.SetBitmap(self.images['FLAG'])
            self.state = MARKED

        elif self.is_marked():
            self.SetBitmap(self.images['CLOSED'])
            self.state = CLOSED

    def get_neighbor_positions(self, max_row, max_col):
        pattern = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        possible_neighbors = [(self.position[0] - a, self.position[1] - b) for a, b in pattern]
        true_neighbors = [(nx, ny) for nx, ny in possible_neighbors if (0 <= nx < max_row and 0 <= ny < max_col)]
        return true_neighbors

    def is_closed(self):
        return self.state == CLOSED

    def is_marked(self):
        return self.state == MARKED

    def is_open(self):
        return self.state == OPENED
