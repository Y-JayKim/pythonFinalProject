import sys

sys.path.insert(0, './GUI/')
from tkinter import *

class AccountInfo:
    def __init__(self, parent):
        self.master = parent
        self.master.title("Account Information Window")

        # Frames and its styles
        self.top_frame = Frame(self.master)
        self.accinfo_frame = Frame(self.master)

        self.top_frame.grid(row=0, sticky=W + E,pady=(0,10))
        self.accinfo_frame.grid(row=1,padx=(50,0),pady=(0,20))

        self.back_button = Button(self.top_frame, text="<-", width=3, height=1)
        self.back_button.grid(row=0, column=0)

        self.balance_label = Label(self.top_frame, text="Your SIN Number: ")
        self.balance_label.grid(row=0, column=1, padx=(40, 0),pady=(10,0))

        self.saving_button = Label(self.accinfo_frame, text="Account : ", width=10, height=2)


if __name__ == '__main__':
    root = Tk()
    AccountInfo(root)
    mainloop()