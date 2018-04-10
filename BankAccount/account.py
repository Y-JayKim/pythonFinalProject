# Account.py
#
# Abstraction for all Account child class
#
# Yeonjae Kim   A00967079   2A
#

from transaction_log import *
from constant import *
import sys


class Account:
    __NEXT_ACCT_NUM = 10000

    def __init__(self, name, balance=0):
        self.negative_check(balance)
        self.name = name
        self._balance = int(balance)
        self.acc_num = Account.__NEXT_ACCT_NUM
        self.transaction = TransactionLog(self.acc_num)
        self.transaction.write_transaction("deposit:"+str(balance))
        Account.__NEXT_ACCT_NUM += 1

    def withdraw(self, amount):
        self.negative_check(amount)
        if self._balance - amount > 0:
            self._balance = self._balance - amount
            self.transaction.write_transaction("withdraw:"+str(-amount))
        else:
            print("Insufficient Funds")

    def deposit(self, amount):
        self.negative_check(amount)
        self._balance += amount
        self.transaction.write_transaction("deposit:"+str(amount))

    def cheque(self, amount):
        self.negative_check(amount)
        if (self._balance - amount) < CHEQUING_NEGATIVE:
            return False
        else:
            self._balance -= amount
            return True

    @property
    def balance(self):
        return self._balance

    # def change_name(self, new_name):
    #     self.name = str(new_name)

    # checks errors
    def negative_check(self, value):
        try:
            if int(value) < 0:
                print("Value must not be negative number")
                sys.exit(0)
        except ValueError:
            print("This value need to be integer")
            sys.exit(0)

    @property
    def get_transaction(self):
        contents = []
        file = self.transaction.get_transaction()
        for line in file:
            contents.append([content for content in line.split(":")])
        return contents

    def interest(self):
        if self._balance >= SAVING_MINIMUM_AMOUNT:
            self.transaction.write_transaction("interest:" + str(round(self._balance * SAVING_INTEREST_RATE, 2)))
            self._balance += self._balance * SAVING_INTEREST_RATE

    def __str__(self):
        return '{}:{}'.format(str(self.acc_num), str(self._balance))


if __name__ == "__main__":
    a = Account("Yeonjae", 10000)
    print(a)
    a.deposit(10000.12)
    a.withdraw(10000.12)
    for nam, amo, day in a.get_transaction:
        print("%-15s $%-15s @%-15s" % (nam, amo, day))
