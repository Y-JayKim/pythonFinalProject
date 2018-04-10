# main_page.py
#
# main window for Account.py
#
# Yeonjae Kim  /  Minsu Song
#

# import sys
# import os
# sys.path.insert(0, '')
from tkinter import *
from tkinter import messagebox
from current_balance import BalanceWindow
from selection import SelectionWindow


class MainWindow:
    def __init__(self, parent):
        self.master=parent
        self.master.title("Main Window")

        # FRAME
        self.left_frame = Frame(self.master)
        self.mid_frame = Frame(self.master)
        self.right_frame = Frame(self.master)

        self.left_frame.grid(column=0, row=0, padx=10, pady=30)
        self.mid_frame.grid(column=1, row=0, padx=10, pady=30)
        self.right_frame.grid(column=2, row=0, padx=10, pady=30)

        # Widgets and Bind to Events
        self.left_top_button = Button(self.left_frame, text="Deposit", width=10, height=5)
        self.left_mid_button = Button(self.left_frame, text="Withdraw", width=10, height=5)
        self.left_bottom_button = Button(self.left_frame, text="Check\nBalance", width=10, height=5)

        self.logo_image = PhotoImage(file="logo.png")
        self.main_image = Label(self.mid_frame, image=self.logo_image, width=70, height=70, cursor="hand2")

        self.right_top_button = Button(self.right_frame, text="Transfer", width=10, height=5)
        self.right_mid_button = Button(self.right_frame, text="Print Account\n Information", width=10, height=5)
        self.right_bottom_button = Button(self.right_frame, text="Help", width=10, height=5)

        # Place Widgets On Window
        # Left
        self.left_top_button.grid(row=0, column=0, padx=5, pady=5)
        self.left_mid_button.grid(row=1, column=0, padx=5, pady=5)
        self.left_bottom_button.grid(row=2, column=0, padx=5, pady=5)

        # Middle
        self.main_image.grid(row=0, column=1, padx=10, pady=5)

        # Right
        self.right_top_button.grid(row=0, column=2, padx=5, pady=5)
        self.right_mid_button.grid(row=1, column=2, padx=5, pady=5)
        self.right_bottom_button.grid(row=2, column=2, padx=5, pady=5)

        self.left_top_button.bind("<Button-1>", self.deposit)
        self.left_mid_button.bind("<Button-1>", self.withdraw)
        self.left_bottom_button.bind("<Button-1>", self.check_balance)
        self.right_top_button.bind("<Button-1>", self.transfer)
        self.right_mid_button.bind("<Button-1>", self.print_info)
        self.right_bottom_button.bind("<Button-1>", self.help)

    def _main_page(self):
        self.newtk = Tk()
        main_window = MainWindow(self.newtk)

        # main_window.left_top_button.bind("<Button-1>", self.deposit)
        # main_window.left_mid_button.bind("<Button-1>", self.withdraw)
        # main_window.left_bottom_button.bind("<Button-1>", self.check_balance)
        # main_window.right_top_button.bind("<Button-1>", self.transfer)
        # main_window.right_mid_button.bind("<Button-1>", self.print_info)
        # main_window.right_bottom_button.bind("<Button-1>", self.help)

    def deposit(self, event):
        self._selection_page('deposit')
        self.action = 1
        return self.action

    def withdraw(self, event):
        self._selection_page('withdraw')
        self.action = 1
        return self.action

    def transfer(self, event):
        self._selection_page('transfer')
        self.action = 1
        return self.action

    def check_balance(self, event):
        self._selection_page('check balance')
        self.action = 2
        return self.action

    def print_info(self, event):
        self._selection_page("print Information")
        self.action = 3
        return self.action

    def help(self, event):
        pass

    def _selection_page(self, option):
        self.master.destroy()
        self.master = Tk()
        selection_window = SelectionWindow(self.master, option)

        selection_window.saving_button.bind("<Button-1>", self._amount_select)
        selection_window.chequing_button.bind("<Button-1>", self._amount_select)

    def _amount_select(self, event):
        if self.action == 1:
            self._balance_page()
        elif self.action == 2:
            messagebox.showinfo("Button", "Balance Check")
        elif self.action == 3:
            messagebox.showinfo("Button", "Information Check")

    def _balance_page(self):
        self.master.destroy()
        self.master = Tk()
        balance_window = BalanceWindow(self.master)
        balance_window.number1_button.config(command="")


if __name__ == "__main__":
    root = Tk()
    MainWindow(root)
    mainloop()
