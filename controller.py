# login_page.py
#
# Log in window for Account.py
#
# Yeonjae Kim  /  Minsu Song
#
import sys
sys.path.insert(0, './GUI/')
from tkinter import *
from tkinter import messagebox
from login_page import LoginWindow
from current_balance import BalanceWindow
from selection import SelectionWindow
from main_page import MainWindow
# from qr_login import BarCodeScanner
import csv
from constant import *


class Controller:
    def __init__(self, parent):
        self.master = parent

        self.LoginWindow = LoginWindow(self.master)
        self.LoginWindow.submit_button.bind("<Button-1>", self._login_page)
        self.LoginWindow.password_entry.bind("<Return>", self._login_page)
        self.LoginWindow.register_lost_label.bind("<Button-1>", self._lost_register)

        self.LoginWindow.qr_button.bind("<Button-1>", self.qr_login)

# ---------------------------------SignIn Page function ----------------------------------------------------
    def _login_page(self, event):
        username = self.LoginWindow.username_entry
        password = self.LoginWindow.password_entry

        if username.get() in self.user_dict and self.user_dict[username.get()] == password.get():
            messagebox.showinfo("Sign In", "Log in Successfully")
            self._main_page()

        else:
            messagebox.showinfo("Invalid", "Invalid username/password")
            username.delete(0, "end")
            password.delete(0, "end")

    def _lost_register(self, event):
        messagebox.showinfo("Info", "Please contact to one of \nour Agent to create/find username")

    def qr_login(self, event):
        # scanner = BarCodeScanner()
        # scanner.start()
        pass

# ---------------------------------Main Page function ----------------------------------------------------
    def _main_page(self):
        self.master.destroy()
        self.master = Tk()
        main_window = MainWindow(self.master)

        main_window.left_top_button.bind("<Button-1>", self.deposit)
        main_window.left_mid_button.bind("<Button-1>", self.withdraw)
        main_window.left_bottom_button.bind("<Button-1>", self.check_balance)
        main_window.right_top_button.bind("<Button-1>", self.transfer)
        main_window.right_mid_button.bind("<Button-1>", self.print_info)
        main_window.right_bottom_button.bind("<Button-1>", self.help)

    def deposit(self, event):
        self._selection_page('deposit')

    def withdraw(self, event):
        self._selection_page('withdraw')

    def transfer(self, event):
        self._selection_page('transfer')

    def check_balance(self, event):
        self._selection_page('check balance')

    def print_info(self, event):
        self._selection_page("print Information")

    def help(self, event):
        pass

# -----------------------------------Selection Page--------------------------------------------------------

    def _selection_page(self, option):
        self.master.destroy()
        self.master = Tk()
        selection_window = SelectionWindow(self.master, option)

        selection_window.saving_button.bind("<Button-1>", self._amount_select)
        selection_window.chequing_button.bind("<Button-1>", self._amount_select)

    def _amount_select(self, event):
        pass
        # self.master.destroy()
        # self.master = Tk()
        # if self.CODE == 1:
        #     BalanceWindow(self.master)
        # elif self.CODE == 2:
        #     messagebox.showinfo("Button", "Balance Check")
        # elif self.CODE == 3:
        #     messagebox.showinfo("Button", "Information Check")

# -------------------------------------------------------------------------------------------
    @property
    def user_dict(self):
        user_file = {}
        with open(USER_ACCOUNT_FILE, 'r') as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                if not row == []:
                    user_file[row[0]] = row[1]
        return user_file


if __name__ == '__main__':
    root = Tk()
    Controller(root)
    mainloop()
