# login_page.py
#
# Log in window for Account.py
#
# Yeonjae Kim  /  Minsu Song
# Transfer feature, QR code, Encryption, sin and pin add or del, print account info, one more button on main,
# Delete number buttons

from tkinter import *
from tkinter import messagebox
from model import Model
import sys
sys.path.insert(0, './GUI/')
from login_page import LoginWindow
from current_balance import BalanceWindow
from selection import SelectionWindow
from main_page import MainWindow
from help_page import Help


class Controller:
    def __init__(self, parent):
        self.master = parent

        self.action = None
        self.data = Model()
        self.data.read_password()
        self.data.read_userinfo()

        self.user_password = self.data.user_password
        self.user_info = self.data.user_dict

        self.LoginWindow = LoginWindow(self.master)
        self.LoginWindow.submit_button.config(command=self._login_page)
        self.LoginWindow.password_entry.bind("<Return>", self._login_page)
        self.LoginWindow.register_lost_label.bind("<Button-1>", self._lost_register)
        self.LoginWindow.qr_button.config(command=self.qr_login)

# ---------------------------------SignIn Page function ----------------------------------------------------
    def _login_page(self, event=None):
        self.sin = self.LoginWindow.username_entry.get()
        self.pin = self.LoginWindow.password_entry.get()

        if self.sin in self.user_password and self.user_password[self.sin] == self.pin:
            messagebox.showinfo("Sign In", "Log in Successfully")
            self._main_page()

        else:
            messagebox.showinfo("Invalid", "Invalid username/password")
            self.LoginWindow.password_entry.delete(0, "end")

    def _lost_register(self):
        messagebox.showinfo("Info", "Please contact to one of \nour Agent to create/find username")

    def qr_login(self):
        messagebox.showinfo("Info", "This feature is currently out of service")

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
        self._selection_page()
        self.action = "deposit"

    def withdraw(self):
        self._selection_page()
        self.action = "withdraw"

    def transfer(self):
        self._selection_page()
        self.action = "transfer"

    def check_balance(self):
        self._selection_page()
        self.action = "balance"

    def print_info(self):
        messagebox.showinfo("Button", "Information Check")
        pass

    def help(self):
        self._help_page()

# -----------------------------------Selection Page--------------------------------------------------------
    def _selection_page(self):
        self.master.destroy()
        self.master = Tk()
        selection_window = SelectionWindow(self.master, self.action)

        for item in self.user_info[self.sin]:
            if 'saving' == repr(item):
                selection_window.saving_button.grid(row=0, column=0, padx=5, pady=5)
            if 'chequing' == repr(item):
                selection_window.chequing_button.grid(row=0, column=1, padx=5, pady=5)
            if 'term saving' == repr(item):
                selection_window.term_saving_button.grid(row=0, column=2, padx=5, pady=5)

        selection_window.saving_button.config(command=self._saving_select)
        selection_window.chequing_button.config(command=self._chequing_select)
        selection_window.term_saving_button.config(command=self._term_saving_select)
        selection_window.back_button.config(command=self._main_page)

    def _saving_select(self):
            self._balance_page('saving')

    def _chequing_select(self):
            self._balance_page('chequing')

    def _term_saving_select(self):
            self._balance_page('term saving')


# ---------------------------------------Current Balance-----------------------------------------
    def _balance_page(self, option):
        self.master.destroy()
        self.master = Tk()

        for item in self.user_info[self.sin]:
            if repr(item) == option:
                self.current_option = option
                self.balance_window = BalanceWindow(self.master, self.action, item.balance)

        if self.action == 'transfer':
            self.balance_window.account_label = Label(self.balance_window.mid1_frame, text="Destination Account")
            self.balance_window.destination_entry = Entry(self.balance_window.mid1_frame, width=20)
            self.balance_window.account_label.grid(row=2, column=1)
            self.balance_window.destination_entry.grid(row=3, column=1)

        self.balance_window.back_button.config(command=self._main_page)
        self.balance_window.confirm_button.config(command=self._confirm_popup)

    def _confirm_popup(self):
        money_entry = int(self.balance_window.input_entry.get())
        accounts = self.user_info[self.sin]
        success = "You just {} ${}".format(self.action, money_entry)
        output = "Invalid Input!"

        for index in range(len(accounts)):
            if repr(accounts[index]) == self.current_option:
                if self.action == 'deposit':
                    accounts[index].balance += money_entry
                    output = success
                elif self.action == 'withdraw':
                    if money_entry < accounts[index].balance:
                        accounts[index].balance -= money_entry
                        output = success

                elif self.action == 'transfer':
                    if str(self.balance_window.destination_entry.get()) in self.user_info and \
                                                                    money_entry < accounts[index].balance:
                        accounts[index].balance -= money_entry
                        output = success

        messagebox.showinfo("Action report", output)
        self._main_page()

    # -----------------------------------Help Page--------------------------------------------------------
    def _help_page(self):
        self.master.destroy()
        self.master = Tk()
        self.main_help_page = Help(self.master)
        self.main_help_page.back_button.config(command=self._main_page)


if __name__ == '__main__':
    root = Tk()
    Controller(root)
    mainloop()
