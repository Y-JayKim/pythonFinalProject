# main_page.py
#
# main window for Account.py
#
# Yeonjae Kim  /  Minsu Song
#
from tkinter import *
# from PIL import ImageTk, Image


class MainWindow:
    def __init__(self, parent):
        self.master = parent
        self.master.title("Main Window")

        # FRAME
        self.left_frame = Frame(self.master)
        self.right_frame = Frame(self.master)

        self.left_frame.grid(column=0, row=0, padx=10, pady=30)
        self.right_frame.grid(column=2, row=0, padx=10, pady=30)

        # Widgets and Bind to Events
        self.left_top_button = Button(self.left_frame, text="Deposit", width=10, height=5)
        self.left_mid_button = Button(self.left_frame, text="Withdraw", width=10, height=5)
        self.left_bottom_button = Button(self.left_frame, text="Check\nBalance", width=10, height=5)

        self.right_top_button = Button(self.right_frame, text="Transfer", width=10, height=5)
        self.right_mid_button = Button(self.right_frame, text="Show Account\n Information", width=10, height=5)
        self.right_bottom_button = Button(self.right_frame, text="Help", width=10, height=5)

        # Place Widgets On Window
        # Left
        self.left_top_button.grid(row=0, column=0, padx=5, pady=5)
        self.left_mid_button.grid(row=1, column=0, padx=5, pady=5)
        self.left_bottom_button.grid(row=2, column=0, padx=5, pady=5)

        # Right
        self.right_top_button.grid(row=0, column=2, padx=5, pady=5)
        self.right_mid_button.grid(row=1, column=2, padx=5, pady=5)
        self.right_bottom_button.grid(row=2, column=2, padx=5, pady=5)


if __name__ == "__main__":
    root = Tk()
    MainWindow(root)
    mainloop()
