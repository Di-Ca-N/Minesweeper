import wx


class GeneralMenu(wx.MenuBar):
    def __init__(self, *args, **kwargs):
        super(GeneralMenu, self).__init__(*args, **kwargs)
        self.Append(FileMenu(), '&File')
        self.Append(HelpMenu(), '&Help')


class FileMenu(wx.Menu):
    def __init__(self, *args, **kwargs):
        super(FileMenu, self).__init__(*args, **kwargs)
        new_game = self.Append(wx.ID_ANY, "&New Game\tCtrl+N", "Starts a new game")
        self.Bind(wx.EVT_MENU, self.on_new_game, new_game)

    def on_new_game(self, event):
        self.GetWindow().restart_game()


class HelpMenu(wx.Menu):
    def __init__(self, *args, **kwargs):
        super(HelpMenu, self).__init__(*args, **kwargs)

        help = self.Append(wx.ID_ANY, "&Help\tCtrl+Q", "How to Play")
        about = self.Append(wx.ID_ANY, "&About", "About the game")

        self.Bind(wx.EVT_MENU, self.display_help, help)
        self.Bind(wx.EVT_MENU, self.display_about, about)

    def display_help(self, event):
        wx.MessageBox(
            "A left click in a cell opens it; a right click marks it as a bomb.\n"
            "The number on each cell is the quantity of bombs around it.\n"
            "The game ends when you mark all bombs or open one of them.",
            "How to Play?",
            wx.OK,
            None
        )

    def display_about(self, event):
        wx.MessageBox(
            "Minesweeper Game developed by Diego Cardoso Nunes\n"
            "Visit the GitHub page for more information: https://github.com/Di-Ca-N/Minesweeper/",
            "About",
            wx.OK,
            None
        )
