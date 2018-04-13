from constant import *
import getpass


class ChangePasswordView:
    def __init__(self, user_password):
        self.user_password = user_password
        self.info = None
        username = input("Please enter the SIN:  ")
        if username in self.user_password:
            password = getpass.getpass("Current Password:  ")
            if password == self.user_password[username]:
                new_password = getpass.getpass('New Password:  ')
                new_password2 = getpass.getpass("Re-New Password:  ")
                if new_password == new_password2:
                    self.info = [username, new_password]
                    print('\nPassword has been changed\n')
                else:
                    print("\nPassword does not match\n")
            else:
                print('\nInvalid Password\n')
        else:
            print('\nThere is no {} in the list\n'.format(username))


if __name__ == '__main__':
    ChangePasswordView({111111111: 'saving'})