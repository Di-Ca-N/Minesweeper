import wx

MARKED = 'marked'
CLOSED = 'closed'
OPENED = 'opened'
DEFAULT_KWARGS = {'style': wx.NO_BORDER}


class Cell(wx.Button):
    def __init__(self, value, position, state=CLOSED, *args, **kwargs):
        kwargs = dict(DEFAULT_KWARGS, **kwargs) # Dict Union
        super(Cell, self).__init__(*args, **kwargs)

        self.value = value
        self.position = position
        self.state = state

        self.SetBackgroundColour(wx.LIGHT_GREY)

    def __repr__(self):
        return "Cell(value={}, position={}, state={})".format(self.value, self.position, self.state)

    def open(self):
        if self.value != '0':
            self.SetLabel(self.value)

        if self.value == '*':
            self.SetBackgroundColour(wx.RED)
        else:
            self.SetBackgroundColour(wx.YELLOW)

        self.state = OPENED
        return self.value

    def toggle_mark(self):
        if self.state == CLOSED:
            self.SetBackgroundColour(wx.RED)
            self.state = MARKED
        elif self.state == MARKED:
            self.SetBackgroundColour(wx.LIGHT_GREY)
            self.state = CLOSED

    def is_neighbor(self, other):
        if other is None:
            return False

        really_x_neighbor = other.position[0] in (self.position[0]-1, self.position[0], self.position[0]+1)
        really_y_neighbor = other.position[1] in (self.position[1]-1, self.position[1], self.position[1]+1)

        return really_x_neighbor and really_y_neighbor

    def get_neighbor_positions(self, max_row, max_col):
        pattern = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        cell_x = self.position[0]
        cell_y = self.position[1]
        possible_neighbors = [(cell_x - a, cell_y- b) for a, b in pattern]
        true_neighbors = [(nx, ny) for nx, ny in possible_neighbors if (0 <= nx < max_row and 0 <= ny < max_col)]
        return true_neighbors

    def is_closed(self):
        return self.state == CLOSED

    def is_marked(self):
        return self.state == MARKED

    def is_open(self):
        return self.state == OPENED
