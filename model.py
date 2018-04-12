# login_page.py
#
# Log in window for Account.py
#
# Yeonjae Kim  /  Minsu Song
#
import sys
from constant import *
import csv
from operator import itemgetter
sys.path.insert(0, './BankAccount/')
from chequing import Chequing
from saving import Saving
from term_saving import TermSaving


class Model:
    def __init__(self):
        self.user_dict = {}
        self.user_password = {}
        self.manager_account = {}

        self._read_userinfo()
        self._read_password()
        self._read_manager_account()

    def _read_userinfo(self):
        with open(USER_INFO_FILE, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                if not row == []:
                    if row[2] not in self.user_dict:
                        self.user_dict[row[2]] = []

                    if row[1] == 'chequing':
                        self.user_dict[row[2]].append(Chequing(row[2], int(row[3])))
                    elif row[1] == 'saving':
                        self.user_dict[row[2]].append(Saving(row[2], int(row[3])))
                    elif row[1] == 'term saving':
                        self.user_dict[row[2]].append(TermSaving(row[2], int(row[3])))

    def write_userinfo(self):
        listoflist = []

        for key in self.user_dict:
            for value in self.user_dict[key]:
                listoflist.append([value.acc_num, repr(value), key, value.balance])
        listoflist = sorted(listoflist, key=itemgetter(0))

        with open(USER_INFO_FILE, 'w') as file:
            csv_writer = csv.writer(file)

            for li in listoflist:
                csv_writer.writerow(li)

    def _read_manager_account(self):
        with open(MANAGER_ACCOUNT_FILE, 'r') as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                self.manager_account[row[0]] = row[1]

    def read_log(self):
        pass

    def write_log(self):
        pass

    def _read_password(self):
        with open(USER_ACCOUNT_FILE, 'r') as file:
            data = csv.reader(file)
            for row in data:
                if row:
                    self.user_password[row[0]] = row[1]

    def write_password(self, identity, password):
        self.user_password[identity] = password
        with open(USER_ACCOUNT_FILE, 'w') as file:
            data = csv.writer(file)
            for key in self.user_password:
                data.writerow([key, self.user_password[key]])


if __name__ == '__main__':
    m = Model()

