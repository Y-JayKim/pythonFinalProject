from constant import *


class TransactionView:
    def __init__(self, user_dict):
        self.user_dict = user_dict

        try:
            self.sin = input("Please Enter the SIN:\t")
        except ValueError:
            print("\nInvalid SIN Number! Please try again later.\n")

        if self.sin in self.user_dict:
            account_choice = input('Please enter account you want to show transactions:\t')
            for account in self.user_dict[self.sin]:
                if account_choice == repr(account):
                    for nam, amo, day in account.get_transaction:
                        print("%-15s $%-15s @%-15s" % (nam, amo, day))
        else:
            print('\nThe Client that matches with the SIN does not exist \n')


if __name__ == '__main__':
    TransactionView({111111111: 'saving'})
