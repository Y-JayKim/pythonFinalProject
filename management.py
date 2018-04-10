# management.py
#
# management CLI interface
#
# Yeonjae Kim   Minsu Song
#
import json
from pprint import pprint
import csv
import json
from constant import *
import sys
sys.path.insert(0, './BankAccount/')
from chequing import Chequing
from saving import Saving
from term_saving import TermSaving


# global
user_dict = {}
user_save_dict = {}


def manager_account():
    manager = {}
    with open(MANAGER_ACCOUNT_FILE, 'r') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            manager[row[0]] = row[1]
    return manager


#------------------------Save and load file----------------------------
def save_file():
    global user_dict
    global user_save_dict

    value_placeholder = ''

    for key in user_dict:
        for value in user_dict[key]:
            value_placeholder += str(value) + ':'
        user_save_dict[key] = value_placeholder
        value_placeholder = ''

    with open(USER_INFO_FILE, 'w') as file:
        file.write(json.dumps(user_save_dict))


def load_file():
    global user_dict

    with open(USER_INFO_FILE, 'r') as file:
        user_dict = json.loads(file.read())

    print(user_dict)


#--------------------------------------------------------------------
def sin_check():
    try:
        sin = int(input("Please Enter the SIN:\t"))

        return str(sin)
    except ValueError:
        print("\nInvalid SIN Number! Please try again later.\n")


#------------------ Creating Account---------------------------------
def create():
    sin = sin_check()

    if len(str(sin)) == 9:
        account_selection = input("Which account do you want to create?:\t")

        for account in ACCOUNTS:
            if account == account_selection:
                create_account(sin, account)
                save_file()
                return True
        print('\nWrong account. Please Select One of These: {}\n'.format(ACCOUNTS))

    else:
        print("\nInvalid SIN number.\n")


def create_account(sin, account):
    global user_dict

    if sin not in user_dict:
        name = input("Please enter the name of the client:\t")
        user_dict[sin] = []
    else:
        name = user_save_dict[sin].split('::')[0]

    if account == 'chequing':
        user_dict[sin].append(Chequing(name))
    elif account == 'saving':
        user_dict[sin].append(Saving(name))
    elif account == 'term saving':
        user_dict[sin].append(TermSaving(name))
    else:
        print('Erorr!! Handling is needed')
    print(user_dict)


def delete_account():
    sin = sin_check()

    if sin in user_dict:
        account_choice = input('Please enter account you want to delete:\t')

        for account in user_dict[sin]:
            if account_choice == repr(account):
                user_dict[sin].remove(account)
        save_file()

    else:
        print('\nThe Client that matches with the SIN does not exist \n')

    print(user_dict)


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


# def account_detail():
#     """Shows account info such as account number, balance and name"""
#
#     username = str(input("Please Enter a username: "))
#     if not username in user_dict:
#         print("The username does not exist")
#         return False
#
#     acc_detail=Account(username)


def main(manage_account):
    # load_file()

    print("--------------------------------------------------------------------\n")
    print("--------------------------------------------------------------------\n")
    print("Hello, this program is for managing bank account\n")
    print("--------------------------------------------------------------------\n")
    print("--------------------------------------------------------------------\n\n")
    print("Please Enter your username and password\n")
    username = input("Username:  ")
    password = input("Password:  ")

    while username != '' and password != '':
        if username in manage_account and password == manage_account[username]:
            print("Please select an option\n\n")
            print("1.Create an User Account    | 2.Delete existing User Account \n3.User's Transaction Report | " \
                  + "4.Detail information of an Account \n5.open a new account        | 0.Exit\n\n")
            selection = input("Please Enter a Number above: ")
            while selection != '':
                if selection == '1':
                    create()
                    selection = '6'
                elif selection == '2':
                    delete_account()
                    selection = '6'
                elif selection == '3':
                    show_transaction()
                    selection = '6'
                elif selection == '4':
                    # account_detail()
                    pass
                elif selection == '5':
                    # transaction()
                    pass
                elif selection == '6':
                    print("1.Create an User Account  | 2.Delete a exist User Account \n3.Report on User          | "\
                          + "4.Detail information of an Account \n5.open a new account       | 0.Exit\n")
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
            password = input("Password:  ")

    print("\nThank you for using Management Program!")


if __name__ == '__main__':
    # read_user()
    main(manager_account())
