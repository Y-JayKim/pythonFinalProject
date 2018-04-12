# transfer_page.py
#
# little more function added from current_balance
#
# Yeonjae Kim  /  Minsu Song
#
from tkinter import *
from current_balance import BalanceWindow


class TransferWindow(BalanceWindow):
    def __init__(self, parent, option, balance=0):
        super().__init__(parent, option, balance)

        self.account_label = Label(self.mid1_frame, text="Destination Account")
        self.destination_entry = Entry(self.mid1_frame, width=20)

        self.account_label.grid(row=2, column=1)
        self.destination_entry.grid(row=3, column=1)


if __name__ == '__main__':
    root = Tk()
    TransferWindow(root, "deposit")
    mainloop()
