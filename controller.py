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
from balance_display import AccountBalance
from account_info_show import AccountInfo
from model import Model


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
        if len(self.user_info[self.sin]) > 0:
            for item in self.user_info[self.sin]:
                if 'saving' == repr(item):
                    self.action_acc_num = item.acc_num
                    self.acc_saving = str(repr(item))
                    selection_window.saving_button.grid(row=0, column=0, padx=5, pady=5)
                if 'chequing' == repr(item):
                    self.action_acc_num=str(item.acc_num)
                    self.acc_saving=str(repr(item))
                    selection_window.chequing_button.grid(row=0, column=1, padx=5, pady=5)
                if 'term saving' == repr(item):
                    self.action_acc_num = item.acc_num
                    self.acc_saving = str(repr(item))
                    selection_window.term_saving_button.grid(row=0, column=2, padx=5, pady=5)

        if self.action == "print_info":
            selection_window.saving_button.config(command=self._account_history_termsaving)
            selection_window.chequing_button.config(command=self._account_history_termsaving)
            selection_window.term_saving_button.config(command=self._account_history_termsaving)
        else:
            selection_window.saving_button.config(command=self._saving_select)
            selection_window.chequing_button.config(command=self._saving_select)
            selection_window.term_saving_button.config(command=self._saving_select)
        selection_window.back_button.config(command=self._main_page)

    #이거 이렇게 해도 가능한가요?? line 125~127 하고 130~140 체크부탁드릴게요
    def _saving_select(self):
            self._amount_type_page(self.acc_saving)
            # self._amount_type_page('saving')

    # def _chequing_select(self):
    #     self._amount_type_page(self.acc_saving)
        # self._amount_type_page('chequing')

    # def _term_saving_select(self):
    #     self._amount_type_page(self.acc_saving)
        # self._amount_type_page('term saving')

    def _account_history_termsaving(self):
        self.master.destroy()
        self.master = Tk()
        acc_window_back=AccountInfo(self.master,self.acc_saving)
        acc_window_back.back_button.config(command=self._main_page)

        transaction_log = self.data.read_write_log(self.action_acc_num)
        for each_log in transaction_log:
            each_line=("You {} ${} on {}".format(each_log[0], each_log[1], each_log[-1]))
            acc_window_back.name_listbox.insert(0, each_line)

# ---------------------------------------Amount Input-----------------------------------------
    def _amount_type_page(self, option):
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
            self.balance_window.destination_entry.bind("<Button-1>", self.balance_window.callback)

        self.balance_window.back_button.config(command=self._main_page)
        self.balance_window.confirm_button.config(command=self._confirm_popup)

    def _confirm_popup(self):
        money_entry = int(self.balance_window.input_entry.get())
        accounts = self.user_info[self.sin]
        success = "You just {} ${}".format(self.action, money_entry)
        output = "Invalid Input!"
        dest = ''

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
                    destination_entry = str(self.balance_window.destination_entry.get())

                    if 1000 <= int(destination_entry) <= self.max_account and \
                                                                money_entry < accounts[index].balance:
                        for num in self.user_info:
                            for account in self.user_info[num]:
                                if account.acc_num == int(destination_entry):
                                    account.balance -= money_entry
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
