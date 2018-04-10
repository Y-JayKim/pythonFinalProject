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
from main_menu import MainMenu
from help_page import Help
# from qr_login import BarCodeScanner
import csv
from constant import *


class Controller:
    def __init__(self, parent):
        self.master = parent

        self.action = 0

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
        self.action = 1
        MainMenu(self.master).file_menu.add_command(label="New Window", command=self._main_page)
        return self.action

    def withdraw(self, event):
        self._selection_page('withdraw')
        self.action = 1
        MainMenu(self.master).file_menu.add_command(label="New Window", command=self._main_page)
        return self.action

    def transfer(self, event):
        self._selection_page('transfer')
        self.action = 1
        MainMenu(self.master).file_menu.add_command(label="New Window", command=self._main_page)
        return self.action

    def check_balance(self, event):
        self._selection_page('check balance')
        self.action = 2
        MainMenu(self.master).file_menu.add_command(label="New Window", command=self._main_page)
        return self.action

    def print_info(self, event):
        self._selection_page("print Information")
        self.action = 3
        MainMenu(self.master).file_menu.add_command(label="New Window", command=self._main_page)
        return self.action

    def help(self, event):
        self._open_help_page()

# -----------------------------------Selection Page--------------------------------------------------------
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

# ---------------------------------------Current Balance-----------------------------------------
    def _balance_page(self):
        self.master.destroy()
        self.master = Tk()

        balance_window = BalanceWindow(self.master)
        MainMenu(self.master).file_menu.add_command(label="New Window", command=self._main_page)
        balance_window.number1_button.config(command="")

    # -----------------------------------Help Page--------------------------------------------------------
    def _open_help_page(self):
        self.master.destroy()
        self.master = Tk()
        Help(self.master)
        MainMenu(self.master).file_menu.add_command(label="New Window", command=self._main_page)


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
