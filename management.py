# management.py
#
# management CLI interface
#
# Yeonjae Kim   Minsu Song
#

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


def manager_account():
    manager = {}
    with open(MANAGER_ACCOUNT_FILE, 'r') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            manager[row[0]] = row[1]
    return manager


# def read_user():
#     global user_dict
#     global userInfo_dict
#
#     with open(USER_ACCOUNT_FILE, 'r') as file:
#         csv_file = csv.reader(file)
#         for row in csv_file:
#             if row != []:
#                 user_dict[row[0]] = row[1]
#
#     with open(USER_INFO_FILE, 'r') as file2:
#         json_file = file2.read()
#         userInfo_dict = json.dumps(json_file)


# def write_user():
#     global user_dict
#     with open(USER_ACCOUNT_FILE, 'w') as file:
#         csv_file = csv.writer(file)
#         for key in user_dict:
#             csv_file.writerow([key, user_dict[key]])
#     read_user()


# def write_userInfo():
#     account[account_num] = ['Started']
#     with open(account_num, 'w') as file:
#         csv_file = csv.writer(file)
#         for key in user_dict:
#             csv_file.writerow([key, user_dict[key]])
#     read_user()


#------------------ Creating Account---------------------------------
def create():
    try:
        sin = int(input("Please Enter a SIN number: "))

        if len(str(sin)) == 9:
            account_selection = input("Which account do you want to create?:\t")

            for account in ACCOUNTS:
                if account == account_selection:
                    create_account(sin, account)
                    return True
            print('\nWrong account. Please Select One of These: {}\n'.format(ACCOUNTS))

        else:
            print("\nInvalid SIN number.\n")
    except ValueError:
        print("\nInvalid SIN Number! Please try again later.\n")


def create_account(sin, account):
    global user_dict

    if sin not in user_dict:
        username = input("Please Enter the Client's Name: ")
        user_dict[sin] = [username]

    username = user_dict[sin][0]

    if account == 'chequing':
        user_dict[sin].append(Chequing(username))
    elif account == 'saving':
        user_dict[sin].append(Saving(username))
    elif account == 'term saving':
        user_dict[sin].append(TermSaving(username))
    else:
        print('Erorr!! Handling is needed')
    print(user_dict)


def delete_account():
    global user_dict
    try:
        sin = int(input("Please Enter SIN you want to delete account from:\t"))

        if sin in user_dict:
            account_choice = input('Please enter account you want to delete:\t')

            for account in user_dict[sin][1:]:
                if account_choice == repr(account):
                    user_dict[sin].remove(account)
        else:
            print('\nThe Client that matches with the SIN does not exist \n')

        print(user_dict)
    except ValueError:
        print("\nInvalid SIN Number! Please try again later.\n")


def transaction_report():
    pass


def account_detail():
    """Shows account info such as account number, balance and name"""

    username = str(input("Please Enter a username: "))
    if not username in user_dict:
        print("The username does not exist")
        return False

    acc_detail=Account(username)


def transaction():
    pass


def main(manage_account):

    print("--------------------------------------------------------------------\n")
    print("--------------------------------------------------------------------\n")
    print("Hello, this program is for managing bank account\n")
    print("--------------------------------------------------------------------\n")
    print("--------------------------------------------------------------------\n\n")
    print("Please Enter your username and password\n")
    username = input("Username:  ")
    password = input("Password:  ")
    # -----------------***********----------
    username = 'root'
    password = 'P@ssw0rd'
    # -----------------***********----------
    while username != '' and password != '':
        if username in manage_account and password == manage_account[username]:
            print("Please select an option\n\n")
            print("1.Create an User Account  | 2.Delete existing User Account \n3.Report on User          | " \
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
                    transaction_report()
                elif selection == '4':
                    account_detail()
                elif selection == '5':
                    transaction()
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
