import sys

sys.path.insert(0, './GUI/')
from tkinter import *

class AccountBalance:
    def __init__(self, parent):
        self.master = parent
        self.master.title("Balance Window")

        # Frames and its styles
        self.top_frame = Frame(self.master)
        self.balance_frame = Frame(self.master, background="white")

        self.top_frame.grid(row=0, sticky=W + E)
        self.balance_frame.grid(row=1,padx=(50,0))

        self.back_button = Button(self.top_frame, text="<-", width=3, height=1)
        self.back_button.grid(row=0, column=0)

        self.balance_label = Label(self.top_frame, text="Your Balance")
        self.balance_label.grid(row=0, column=1, padx=(40, 0))

        self.saving_button = Label(self.balance_frame, text="Saving: ", width=10, height=5)
        self.chequing_button = Label(self.balance_frame, text="Chequing: ", width=10, height=5)
        self.term_saving_button = Label(self.balance_frame, text="Term Saving: ", width=10, height=5)


if __name__ == '__main__':
    root = Tk()
    AccountBalance(root)
    mainloop()