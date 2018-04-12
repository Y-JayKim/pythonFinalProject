# selection.py
#
# selection window for Account.py
#
# Yeonjae Kim  /  Minsu Song
#
from tkinter import *


class SelectionWindow:
    def __init__(self, parent, option):
        self.master = parent
        self.master.title("selection Window")

        # Frame
        self.top_frame = Frame(self.master)
        self.bottom_frame = Frame(self.master)

        self.top_frame.grid(row=0)
        self.bottom_frame.grid(row=1, padx=10, pady=30)

        # Widgets and Bind to Events
        self.explanation_label = Label(self.top_frame, \
                                       text='Please Select Account You want to {}'.format(option))
        self.back_button = Button(self.top_frame, text="<-", width=3, height=1)
        self.saving_button = Button(self.bottom_frame, text="Saving", width=10, height=5)
        self.chequing_button = Button(self.bottom_frame, text="Chequing", width=10, height=5)
        self.term_saving_button = Button(self.bottom_frame, text="Term Saving", width=10, height=5)
        # Place Widgets On Window
        # Top
        self.explanation_label.grid(row=1, column=1, padx=(10,20), pady=5)
        self.back_button.grid(row=0, column=0)

        # Bottom
        # self.saving_button.grid(row=0, column=0, padx=5, pady=5)
        # self.chequing_button.grid(row=0, column=1, padx=5, pady=5)


if __name__ == "__main__":
    root = Tk()
    SelectionWindow(root, "Deposit")
    mainloop()
