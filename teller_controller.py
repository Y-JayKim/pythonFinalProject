# teller_controller.py
#
# Description
#
# Yeonjae Kim  /  Minsu Song
#

from model import *
from constant import *
from model import Model

import sys
sys.path.insert(0, './BankAccount/')
from chequing import Chequing
from saving import Saving
from term_saving import TermSaving
sys.path.insert(0, './CLI')
from create_view import CreateView
from delete_view import DeleteView
from transaction_view import TransactionView
from changePassword_view import ChangePasswordView
from teller_SelectionView import ManageSelection
from teller_LoginView import ManagementLogin


class TellerController:
    def __init__(self):
        self.model = Model()
        self.user_dict = self.model.user_dict
        self.user_password = self.model.user_password
        self.manage_account = self.model.manager_account
        self._sin = None

        first_page = ManagementLogin()
        first_page.asking_username()

        while first_page.username != '' and first_page.password != '':
            if first_page.username in self.manage_account and first_page.password == self.manage_account[first_page.username]:
                second_page = ManageSelection()
                second_page.selection_page()

                while second_page.selection != '':
                    if second_page.selection == '1':
                        self.create()
                        second_page.selection = '5'
                    elif second_page.selection == '2':
                        self.delete_account()
                        second_page.selection = '5'
                    elif second_page.selection == '3':
                        self.show_transaction()
                        second_page.selection = '5'
                    elif second_page.selection == '4':
                        self.change_password()
                        second_page.selection = '5'
                    elif second_page.selection == '5':
                        second_page.selection_page()
                    elif second_page.selection == '0' or second_page.selection == 'exit':
                        break
                    else:
                        second_page.not_in_option()
                    self._save_file()
                break
            else:
                first_page.wrong_password()

    def _save_file(self):
        self.model.write_userinfo()
        print(self.user_dict)

    def create(self):
        new_account = CreateView(self.user_dict)
        sin = new_account.sin
        account_type = new_account.account_type
        current_account = ''

        if sin and account_type:
            if account_type == 'chequing':
                current_account = Chequing(sin)
                self.user_dict[sin].append(current_account)
            elif account_type == 'saving':
                current_account = Saving(sin)
                self.user_dict[sin].append(current_account)
            elif account_type == 'term saving':
                current_account = TermSaving(sin)
                self.user_dict[sin].append(current_account)

            new_account.notice()

            if sin not in self.user_password:
                self.model.write_password(sin, '123')
            self.model.write_log(current_account.acc_num)


    def delete_account(self):
        remove_account = DeleteView(self.user_dict)
        info = remove_account.deletion_info

        if info:
            self.user_dict[info['sin']][int(info['ind'])].name = 000000000
            self.user_dict['000000000'].append(self.user_dict[info['sin']][int(info['ind'])])
            self.user_dict[info['sin']].pop(int(info['ind']))

    def show_transaction(self):
        TransactionView(self.user_dict)

    def change_password(self):
        new_password = ChangePasswordView(self.user_password)
        if new_password.info:
            self.model.write_password(new_password.info[0], new_password.info[1])



if __name__ == '__main__':
    t = TellerController()
