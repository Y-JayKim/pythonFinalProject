from constant import *


class CreateView:
    def __init__(self, user_dict):
        self.account_type = None
        self.sin = None
        self.account_selection = None
        self.user_dict = user_dict
        try:
            self.sin = input("Please Enter the SIN:\t")
        except ValueError:
            print("\nInvalid SIN Number! Please try again later.\n")

        if len(self.sin) == 9:
            self._selection_check()
        else:
            print("\nInvalid SIN number.\n")

    def _selection_check(self):
            self.account_selection = input("Which account do you want to create?:\t")

            for account in ACCOUNTS:
                if account == self.account_selection:
                    if len(self.user_dict) != 0:
                        self._create_account(account)
                    return
            print('\nWrong account. Please Select One of These: {}\n'.format(ACCOUNTS))

    def _create_account(self, account_option):
        if self.sin not in self.user_dict:
            self.user_dict[self.sin] = []
            self.
        for account in self.user_dict[self.sin]:
            if account_option == repr(account):
                print('\nThe client already has {} account\n'.format(repr(account)))
                return
        self.account_type = account_option

    def notice(self):
        print("\n{} account has been added to SIN {}\n".format(self.account_type, self.sin))


if __name__ == '__main__':
    CreateView({111111111: 'saving'})
