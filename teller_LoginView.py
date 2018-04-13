import getpass


class ManagementLogin:
    def __init__(self):
        self.username = ''
        self.password = ''
        print("--------------------------------------------------------------------\n")
        print("--------------------------------------------------------------------\n")
        print("Hello, this program is for managing bank account\n")
        print("--------------------------------------------------------------------\n")
        print("--------------------------------------------------------------------\n\n")

    def asking_username(self):
        print("Please Enter your username and password\n")
        self.username = input("Username:  ")
        self.password = getpass.getpass("Password:  ")

    def wrong_password(self):
        print("\nWrong password!\n")
        print("Please Enter your username and password again\n")
        self.username = input("Username:  ")
        self.password = getpass.getpass("Password:  ")