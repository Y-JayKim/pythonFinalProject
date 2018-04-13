# model.py
#
# File opening and writing
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
sys.path.insert(0, './GUI/')
from account_info_show import AccountInfo


class Model:
    def __init__(self):
        pass
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
        if '000000000' not in self.user_dict:
            self.user_dict['000000000'] = []

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
                self.manager_account[self.decrypting_letters(row[0])] = self.decrypting_letters(row[1])

    def _read_log(self, acc_num):
        file= open(acc_num+"_log.txt")
        history = file.readlines()
        file.close()
        names = [name.split("::") for name in history]
        for name in names:
            AccountInfo.name_listbox.insert(-1, name)

    def write_log(self):
        pass

    def _read_password(self):
        with open(USER_ACCOUNT_FILE, 'r') as file:
            data = csv.reader(file)
            for row in data:
                if row:
                    self.user_password[self.decrypting_letters(str(row[0]))] = self.decrypting_letters(str(row[1]))

    def write_password(self, identity, passwrd):
        encrypted_password = {}

        self.user_password[identity] = passwrd

        for user in self.user_password:
            user_encoded = self.encrypting_letters(user)
            pass_encoded = self.encrypting_letters(self.user_password[user])

            encrypted_password[user_encoded] = pass_encoded

        with open(USER_ACCOUNT_FILE, 'w') as file:
            data = csv.writer(file)
            for key in encrypted_password:
                data.writerow([key, encrypted_password[key]])

    def encrypting_letters(self, letter):
        outcome = ''
        for i in letter:
            outcome += str(ord(i))+':'
        return outcome[:-1]

    def decrypting_letters(self, letter):
        outcome = ''
        letter_list = letter.split(':')
        for i in letter_list:
            outcome += chr(int(i))
        return outcome


if __name__ == '__main__':
    m = Model()