# Transaction_Log.py
#
# Saves transactions from accounts
#
# Yeonjae Kim   A00967079   2A
#
import datetime


class TransactionLog:
    def __init__(self, acc_num):
        self.transaction_num = acc_num
        self.timeDate = datetime.datetime.now()

    def get_transaction(self):
        with open(str(self.transaction_num) + '_log.txt', 'r') as file:
            content = file.read()
        return content.split("::")[:-1]

    def write_transaction(self, value=None):
        with open(str(self.transaction_num)+'_log.txt', 'a') as file:
            if value is not None:
                file.write(str(value)+":"+str(self.timeDate)[:10]+"::")


if __name__ == "__main__":
    t = TransactionLog(10004)
