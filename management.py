# management.py
#
# management CLI interface
#
# Yeonjae Kim   Minsu Song
#
import csv
from operator import itemgetter
from constant import *
from model import Model
import getpass
import sys
sys.path.insert(0, './BankAccount/')
from chequing import Chequing
from saving import Saving
from term_saving import TermSaving


# global
model = Model()
user_dict = model.user_dict
user_password = model.user_password
manage_account = model.manager_account


#------------------------Save and load file----------------------------
def save_file():
    global model
    model.write_userinfo()


#--------------------------------------------------------------------
def sin_check():
    try:
        sin = int(input("Please Enter the SIN:\t"))

        return str(sin)
    except ValueError:
        print("\nInvalid SIN Number! Please try again later.\n")


def exist_account(account_choice, sin):
    global user_dict

    for account in user_dict[sin]:
        if account_choice == repr(account):
            return True
    return False


#------------------ Creating Account---------------------------------
def create():
    sin = sin_check()

    if len(str(sin)) == 9:
        account_selection = input("Which account do you want to create?:\t")

        for account in ACCOUNTS:
            if account not in user_dict and account == account_selection:
                create_account(sin, account)
                save_file()
                return True

        print('\nWrong account. Please Select One of These: {}\n'.format(ACCOUNTS))

    else:
        print("\nInvalid SIN number.\n")


def create_account(sin, account):
    global user_dict

    if sin not in user_dict:
        user_dict[sin] = []

    if not exist_account(account, sin):
        if account == 'chequing':
            user_dict[sin].append(Chequing(sin))
        elif account == 'saving':
            user_dict[sin].append(Saving(sin))
        elif account == 'term saving':
            user_dict[sin].append(TermSaving(sin))
        else:
            print('Erorr!! Handling is needed')
    else:
        print('\nThe client already has {} account\n'.format(account))

    print(user_dict)


#------------------ Deleting Account---------------------------------
def delete_account():
    sin = sin_check()

    if sin in user_dict:
        account_choice = input('Please enter account you want to delete:\t')
        for account in user_dict[sin]:
            if account_choice == repr(account):
                user_dict[sin].remove(account)
                save_file()
                return True

        print("There is no existing account")
    else:
        print('\nThe Client that matches with the SIN does not exist \n')

    print(user_dict)


#------------------Show Account Detail---------------------------------
def show_transaction():
    global user_dict
    sin = sin_check()

    if sin in user_dict:
        account_choice = input('Please enter account you want to show transactions:\t')

        for account in user_dict[sin]:
            if account_choice == repr(account):
                a = account
                for nam, amo, day in a.get_transaction:
                    print("%-15s $%-15s @%-15s" % (nam, amo, day))

    else:
        print('\nThe Client that matches with the SIN does not exist \n')


#-------------------Change password for a pin------------------------
def change_password():
    username = input("Please enter the SIN:  ")
    password = getpass.getpass("Password:  ")


#-------------------------------Main---------------------------------
def main():
    global manage_account

    print("--------------------------------------------------------------------\n")
    print("--------------------------------------------------------------------\n")
    print("Hello, this program is for managing bank account\n")
    print("--------------------------------------------------------------------\n")
    print("--------------------------------------------------------------------\n\n")
    print("Please Enter your username and password\n")
    username = input("Username:  ")
    password = getpass.getpass("Password:  ")

    while username != '' and password != '':
        if username in manage_account and password == manage_account[username]:
            print("Please select an option\n\n")
            print("1.Create an User Account    | 2.Delete existing User Account \n3.User's Transaction Report | "
                  + "4. Change PIN\n5. Show options again       | 0.Exit \n\n")
            selection = input("Please Enter a Number above: ")
            while selection != '':
                if selection == '1':
                    create()
                    selection = '5'
                elif selection == '2':
                    delete_account()
                    selection = '5'
                elif selection == '3':
                    show_transaction()
                    selection = '5'
                elif selection == '4':
                    change_password()
                    selection = '5'
                elif selection == '5':
                    print("\n1.Create an User Account    | 2.Delete existing User Account \n"
                          + "3.User's Transaction Report | 4. Change PIN\n5. Show options again \t    | 0.Exit\n\n")
                    selection = input("Please Enter a Number above: ")
                elif selection == '0' or selection == 'exit':
                    break
                else:
                    print("\nInvalid Input. Please try again.\n")
                    print("Enter 6 to see the menu again\n")
                    selection = input("Please Enter a Number: ")
            break
        else:
            print("\nWrong password!\n")
            print("Please Enter your username and password again\n")
            username = input("Username:  ")
            password = getpass.getpass("Password:  ")

    print("\nThank you for using Management Program!")


if __name__ == '__main__':
    main()
