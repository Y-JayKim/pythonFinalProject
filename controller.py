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
from transfer_page import TransferWindow
from help_page import Help
# from qr_login import BarCodeScanner
import csv
from constant import *


class Controller:
    def __init__(self, parent):
        self.master = parent

        self.action = None

        self.LoginWindow = LoginWindow(self.master)
        self.LoginWindow.submit_button.config(command=self._login_page)
        self.LoginWindow.password_entry.bind("<Return>", self._login_page)
        self.LoginWindow.register_lost_label.bind("<Button-1>", self._lost_register)
        self.LoginWindow.qr_button.config(command=self.qr_login)

# ---------------------------------SignIn Page function ----------------------------------------------------
    def _login_page(self, event=None):
        username = self.LoginWindow.username_entry
        password = self.LoginWindow.password_entry

        if username.get() in self.user_dict and self.user_dict[username.get()] == password.get():
            messagebox.showinfo("Sign In", "Log in Successfully")
            self._main_page()

        else:
            messagebox.showinfo("Invalid", "Invalid username/password")
            username.delete(0, "end")
            password.delete(0, "end")

    def _lost_register(self):
        messagebox.showinfo("Info", "Please contact to one of \nour Agent to create/find username")

    def qr_login(self):
        # scanner = BarCodeScanner()
        # scanner.start()
        pass

# ---------------------------------Main Page function ----------------------------------------------------
    def _main_page(self):
        self.master.destroy()
        self.master = Tk()
        main_window = MainWindow(self.master)

        main_window.left_top_button.config(command=self.deposit)
        main_window.left_mid_button.config(command=self.withdraw)
        main_window.left_bottom_button.config(command=self.check_balance)
        main_window.right_top_button.config(command=self.transfer)
        main_window.right_mid_button.config(command=self.print_info)
        main_window.right_bottom_button.config(command=self.help)

    def deposit(self):
        self._balance_page('deposit')
        self.action = "deposit"

    def withdraw(self):
        self._balance_page('withdraw')
        self.action = "withdraw"

    def transfer(self):
        self._transfer_page('transfer')
        self.action = "transfer"

    def check_balance(self):
        messagebox.showinfo("Button", "Balance Check")
        pass

    def print_info(self):
        messagebox.showinfo("Button", "Information Check")
        pass

    def help(self):
        self._help_page()

# -----------------------------------Selection Page--------------------------------------------------------
#     def _selection_page(self, option):
#         self.master.destroy()
#         self.master = Tk()
#         selection_window = SelectionWindow(self.master, option)
#
#         selection_window.saving_button.config(command=self._amount_select)
#         selection_window.chequing_button.config(command=self._amount_select)
#         selection_window.back_button.config(command=self._main_page)
#
#     def _amount_select(self):
#         if self.action in ['deposit', 'withdraw', 'transfer']:
#             self._balance_page()
#         elif self.action == 'check_balance':
#             messagebox.showinfo("Button", "Balance Check")
#         elif self.action == 'show_info':
#             messagebox.showinfo("Button", "Information Check")

# ---------------------------------------Current Balance-----------------------------------------
    def _balance_page(self, option):
        self.master.destroy()
        self.master = Tk()

        self.balance_window = BalanceWindow(self.master, option)
        self.balance_window.number1_button.config(command=self._button_action)

        self.balance_window.back_button.config(command=self._main_page)
        self.balance_window.confirm_button.config(command=self._confirm_popup)

    def _transfer_page(self, option):
        self.master.destroy()
        self.master = Tk()

        self.transfer_window = TransferWindow(self.master, option)
        self.transfer_window.number1_button.config(command=self._button_action)

        self.transfer_window.back_button.config(command=self._main_page)
        self.transfer_window.confirm_button.config(command=self._confirm_popup)

    def _confirm_popup(self):
        self.user_type_amount = self.balance_window.input_entry.get()
        messagebox.showinfo("Action report", "You just {} ${}".format(self.action, self.user_type_amount))
        self._main_page()

    def _button_action(self):
        pass

    # -----------------------------------Help Page--------------------------------------------------------
    def _help_page(self):
        self.master.destroy()
        self.master = Tk()
        self.main_help_page = Help(self.master)
        self.main_help_page.back_button.config(command=self._main_page)

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
