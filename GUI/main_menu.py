# main_menu.py
#
# Menu Class for every Window
#
# Yeonjae Kim  /  Minsu Song
#
from tkinter import *


class MainMenu:
    def __init__(self, parent):
        self.master = parent
        self.master.title("Login Window")

        # Calling Menu Widget
        self.main_menu = Menu(self.master)
        self.master.config(menu=self.main_menu)

        # options for menu
        self.file_menu = Menu(self.main_menu)
        self.edit_menu = Menu(self.main_menu)
        self.view_menu = Menu(self.main_menu)
        self.help_menu = Menu(self.main_menu)

        # Cascading
        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.main_menu.add_cascade(label="View", menu=self.view_menu)
        self.main_menu.add_cascade(label="Help", menu=self.help_menu)

        # add command in menus
        self.file_menu.add_command(label="New Window")
        self.file_menu.add_command(label="Import Setting")
        self.file_menu.add_command(label="Print")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)

        # place window on center
        # Gets the requested values of the height and width.
        self._window_width = self.master.winfo_reqwidth()
        self._window_height = self.master.winfo_reqheight()

        # Gets both half the screen width/height and window width/height
        self.position_right = int(self.master.winfo_screenwidth() / 3 - self._window_width / 3)
        self.position_down = int(self.master.winfo_screenheight() / 3 - self._window_height / 3)

        # Positions the window in the center of the page.
        self.master.geometry("+{}+{}".format(self.position_right, self.position_down))


if __name__ == "__main__":
    root = Tk()
    MainMenu(root)
    mainloop()
