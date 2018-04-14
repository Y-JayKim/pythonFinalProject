# balance_display.py
#
# Shows the balance of each account
#
# Yeonjae Kim  /  Minsu Song
#
import sys

sys.path.insert(0, './GUI/')
from tkinter import *


class AccountBalance:
    def __init__(self, parent):
        self.master = parent
        self.master.title("Balance Window")

        # Frames and its styles
        self.top_frame = Frame(self.master)
        self.balance_frame = Frame(self.master)

        self.top_frame.grid(row=0, sticky=W + E,pady=(0,10))
        self.balance_frame.grid(row=1,padx=50,pady=(0,20))

        self.back_button = Button(self.top_frame, text="<-", width=3, height=1)
        self.back_button.grid(row=0, column=0)

        self.balance_label = Label(self.top_frame, text="Your Balance")
        self.balance_label.grid(row=0, column=1, padx=(50, 0),pady=(10,0))

        self.saving_button = Label(self.balance_frame, text="Saving: ", width=10, height=2)
        self.chequing_button = Label(self.balance_frame, text="Chequing: ", width=10, height=2)
        self.term_saving_button = Label(self.balance_frame, text="Term Saving: ", width=10, height=2)


if __name__ == '__main__':
    root = Tk()
    AccountBalance(root)
    mainloop()