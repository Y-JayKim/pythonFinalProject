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
from account_info_show import AccountInfo
from login_page import LoginWindow
from current_balance import BalanceWindow
from selection import SelectionWindow
from main_page import MainWindow
from help_page import Help
from balance_display import AccountBalance


class Controller:
    def __init__(self, parent):
        self.master = parent

        self.action = None
        self.data = Model()

        self.user_password = self.data.user_password
        self.user_info = self.data.user_dict

        self.max_account = 9999
        for person in self.user_info:
            self.max_account += len(self.user_info[person])

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
        self.action = "deposit"
        self._selection_page()

    def withdraw(self):
        self.action = "withdraw"
        self._selection_page()

    def transfer(self):
        self.action = "transfer"
        self._selection_page()

    def check_balance(self):
        self.action = "balance"
        self._balance_page()

    def print_info(self):
        self.action = "print_info"
        self._selection_page()

    def help(self):
        self._help_page()

# -----------------------------------Selection Page--------------------------------------------------------
    def _selection_page(self):
        self.master.destroy()
        self.master = Tk()
        selection_window = SelectionWindow(self.master, self.action)
        exist_account = {}

        if len(self.user_info[self.sin]) > 0:
            for item in self.user_info[self.sin]:
                if 'saving' == repr(item):
                    exist_account["saving"] = item
                    selection_window.saving_button.grid(row=0, column=0, padx=5, pady=5)
                if 'chequing' == repr(item):
                    selection_window.chequing_button.grid(row=0, column=1, padx=5, pady=5)
                    exist_account["chequing"] = item
                if 'term saving' == repr(item):
                    selection_window.term_saving_button.grid(row=0, column=2, padx=5, pady=5)
                    exist_account["term saving"] = item
        else:
            messagebox.showinfo("warning", "You do not have any account!")
            self._main_page()

        if self.action == "print_info":
            selection_window.saving_button.config(command=lambda :self._account_history_termsaving(exist_account["saving"]))
            selection_window.chequing_button.config(command=lambda :self._account_history_termsaving(exist_account["chequing"]))
            selection_window.term_saving_button.config(command=lambda :self._account_history_termsaving(exist_account["term saving"]))
        else:
            selection_window.saving_button.config(command=lambda : self._amount_type_page(exist_account['saving']))
            selection_window.chequing_button.config(command=lambda : self._amount_type_page(exist_account['chequing']))
            selection_window.term_saving_button.config(command=lambda : self._amount_type_page(exist_account['term saving']))

        selection_window.back_button.config(command=self._main_page)

    def _account_history_termsaving(self, acc_item):
        self.master.destroy()
        self.master = Tk()
        acc_window_back = AccountInfo(self.master, repr(acc_item))
        acc_window_back.back_button.config(command=self._main_page)

        transaction_log = self.data.read_write_log(acc_item.acc_num)
        for each_log in transaction_log:
            each_line = ("You {} ${} on {}".format(each_log[0], each_log[1], each_log[-1]))
            acc_window_back.name_listbox.insert(0, each_line)

# ---------------------------------------Amount Input-----------------------------------------
    def _amount_type_page(self, acc_item):
        self.master.destroy()
        self.master = Tk()

        self.balance_window = BalanceWindow(self.master, self.action, acc_item.balance)

        if self.action == 'transfer':
            self.balance_window.account_label = Label(self.balance_window.mid1_frame, text="Destination Account")
            self.balance_window.destination_entry = Entry(self.balance_window.mid1_frame, width=20)
            self.balance_window.account_label.grid(row=2, column=1)
            self.balance_window.destination_entry.grid(row=3, column=1)
            self.balance_window.destination_entry.bind("<Button-1>", self.balance_window.callback)

        self.balance_window.back_button.config(command=self._main_page)
        self.balance_window.confirm_button.config(command=lambda : self._amount_type_page(acc_item))

    def _confirm_popup(self, acc_item):
        money_entry = int(self.balance_window.input_entry.get())
        accounts = self.user_info[self.sin]
        success = "You just {} ${}".format(self.action, money_entry)
        output = "Invalid Input!"
        dest = ''

        if self.action == 'deposit':
            acc_item.balance += money_entry
            output = success
        elif self.action == 'withdraw':
            if money_entry < acc_item.balance:
                acc_item.balance -= money_entry
                output = success

        elif self.action == 'transfer':
            destination_entry = str(self.balance_window.destination_entry.get())

            if 1000 <= int(destination_entry) <= self.max_account and money_entry < acc_item.balance:
                if acc_item.acc_num == int(destination_entry):
                    acc_item.balance -= money_entry
                output = success
                dest = ' to Account {}'.format(destination_entry)

        if output != "Invalid Input!":
            self.data.write_userinfo()
        messagebox.showinfo("Action report", output + dest)
        self._main_page()


    # -----------------------------------Help Page--------------------------------------------------------
    def _help_page(self):
        self.master.destroy()
        self.master = Tk()
        self.main_help_page = Help(self.master)
        self.main_help_page.back_button.config(command=self._main_page)


# ---------------------------------------Balance Display---------------------------------------------
    def _balance_page(self):
        self.master.destroy()
        self.master = Tk()
        self.existing_acc_window = AccountBalance(self.master)

        for item in self.user_info[self.sin]:
            row1 = 0
            if 'saving' == repr(item):
                row1 = 0
                self.existing_acc_window.saving_button.grid(row=row1, column=0, pady=5)
            if 'chequing' == repr(item):
                row1 = 1
                self.existing_acc_window.chequing_button.grid(row=row1, column=0, pady=5)
            if 'term saving' == repr(item):
                row1 = 2
                self.existing_acc_window.term_saving_button.grid(row=row1, column=0, pady=5)

            self.balance_show_label = Label(self.existing_acc_window.balance_frame, text=item.balance)
            self.balance_show_label.grid(row=row1, column=1, pady=10)
        self.existing_acc_window.back_button.config(command=self._main_page)


if __name__ == '__main__':
    root = Tk()
    Controller(root)
    mainloop()
