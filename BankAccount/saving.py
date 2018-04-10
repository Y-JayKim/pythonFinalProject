# Saving.py
#
# Saving class
#
# Yeonjae Kim   A00967079   2A
#
from constant import *
from account import Account
import sys


class Saving(Account):

    def __init__(self, name, balance=1000):
        self.negative_check(balance)
        if int(balance) < 1000:
            print("Saving Account needs at least $1000")
            sys.exit(1)
        super().__init__(name, balance)

    def withdraw(self, amount):
        super().withdraw(amount)
        if self._balance < SAVING_MINIMUM_AMOUNT:
            self._balance += SAVING_FEE
            self.transaction.write_transaction("Fee:" + str(SAVING_FEE))

    def cheque(self, amount=None):
        return False

    def __repr__(self):
        return 'saving'


if __name__ == "__main__":

    a = Saving("Yeonjae", 1000)
    print(a)
    # a.withdraw(1000.12)
    # a.interest()
    # print(a.balance)
    # a.deposit(1000.12)
    # print(a.balance)
    # a.interest()
    # for nam, amo, day in a.get_transaction:
    #     print("%-15s $%-15s @%-15s" % (nam, amo, day))
    # print(a.balance)
