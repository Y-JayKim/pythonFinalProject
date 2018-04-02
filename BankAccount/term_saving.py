# Term_Saving.py
#
# Term_Saving Class
#
# Yeonjae Kim   A00967079   2A
#
from constant import *
from saving import Saving
import datetime
from datetime import date


class TermSaving(Saving):

    def __init__(self, name, balance=1000):
        super().__init__(name, balance)

    def withdraw(self, amount):
        self.negative_check(amount)
        history = {"deposit": 0, "withdraw": 0}

        file = self.transaction.get_transaction()
        for line in file:
            contents = line.split(":")
            year, month, day = contents[2].split("-")
            if contents[0] == "withdraw":
                history[contents[0]] += float(contents[1])
            if contents[0] == "deposit" and date.today() - date(int(year), int(month), int(day)) > datetime.timedelta(60):
                history[contents[0]] += float(contents[1])
        if int(amount) <= history["deposit"] - history["withdraw"]:
            self._balance -= amount
            self.transaction.write_transaction("withdraw:"+str(amount))
        else:
            print("Insufficient Funds")


if __name__ == "__main__":
    a = TermSaving("Jay")
    a.withdraw(1000.0)
    a.withdraw(5000.0)
    for nam, amo, da in a.get_transaction:
        print("%-15s $%-15s @%-15s" % (nam, amo, da))
