# chequing.py
#
# Chequing Class
#
# Yeonjae Kim   A00967079   2A
#
from constant import *
from account import Account
from transaction_log import *


class Chequing(Account):

    def __init__(self, name, balance=0):
        super().__init__(name, balance)

    def withdraw(self, amount):
        self.negative_check(amount)
        if self.cheque(amount):
            self.transaction.write_transaction("withdraw:" + str(amount))
            self.overdraft()
        else:
            print("Insufficient Funds")

    def post_cheque(self, amount):
        self.negative_check(amount)
        if self.cheque(amount):
            self.transaction.write_transaction("cheque:" + str(amount))
            self.overdraft()
        else:
            self._balance += BOUNCED_FEE
            self.transaction.write_transaction("bounced:" + str(BOUNCED_FEE))

    def overdraft(self):
        if self._balance < 0:
            self.transaction.write_transaction("overdraft:" + str(round(self._balance * CHEQUING_OVERDRAFT_FEE, 2)))
            self._balance += round(self._balance * CHEQUING_OVERDRAFT_FEE, 2)

    def interest(self):
        return False

    def __repr__(self):
        return 'chequing'


if __name__ == "__main__":
    a = Chequing("Yeonjae")
    b = Chequing("jay")

    c = [a, b]

    # print(a)
    # a.deposit(10000.12)
    # a.withdraw(1000.12)
    # a.post_cheque(1000.12)
    # print(a.balance)
    # a.post_cheque(1000.12)
    # print(a.balance)
    # for nam, amo, day in a.get_transaction:
    #     print("%-15s $%-15s @%-15s" % (nam, amo, day))

