from constant import *


class DeleteView:
    def __init__(self, user_dict):
        self.user_dict = user_dict
        self.deletion_info = None

        try:
            self.sin = input("Please Enter the SIN:\t")
        except ValueError:
            print("\nInvalid SIN Number! Please try again later.\n")

        self._deletion()

    def _deletion(self):
        if self.sin in self.user_dict:
            account_choice = input('Please enter account you want to delete:\t')
            for ind in range(len(self.user_dict[self.sin])):
                if account_choice == repr(self.user_dict[self.sin][ind]):
                    self.deletion_info = {'sin': self.sin, 'ind': str(ind)}
                    return True

            print("There is no existing account")
        else:
            print('\nThe Client that matches with the SIN does not exist \n')


if __name__ == '__main__':
    DeleteView({111111111: 'saving'})