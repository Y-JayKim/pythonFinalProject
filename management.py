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
from account import *


# global
user_dict = {}
userInfo_dict = {}


def manager_account():
    manager = {}
    with open(MANAGER_ACCOUNT_FILE, 'r') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            manager[row[0]] = row[1]
    return manager


def read_user():
    global user_dict
    global userInfo_dict

    with open(USER_ACCOUNT_FILE, 'r') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            if row != []:
                user_dict[row[0]] = row[1]

    with open(USER_INFO_FILE, 'r') as file2:
        json_file = file2.read()
        userInfo_dict = json.dumps(json_file)

def write_user():
    global user_dict
    with open(USER_ACCOUNT_FILE, 'w') as file:
        csv_file = csv.writer(file)
        for key in user_dict:
            csv_file.writerow([key, user_dict[key]])
    read_user()


def write_userInfo():
    account[account_num] = ['Started']
    with open(account_num, 'w') as file:
        csv_file = csv.writer(file)
        for key in user_dict:
            csv_file.writerow([key, user_dict[key]])
    read_user()


def new_account_to_user(account_type):
    """"add account to the user"""
    pass


def create_account():
    global user_dict
    print(user_dict)
    sin_num = str(input("Please Enter a SIN number: "))
    if sin_num in user_dict:
        print("User name already exists!!")
        return False
    else:
        print('username: {} and Password: {}\n'.format(sin_num, password))
        print("Please type yes or y to continue.\nIf you want to cancel, please enter n or no\n")
        selection = input("---> :")
        if selection == 'y' or selection == 'yes':
            user_dict[sin_num] = password
            write_user()

        elif selection == 'n' or selection == 'no':
            print("Okay ByeBye")
    else:
        print("Those password did not match.")

def delete_user():
    global user_dict

    account_num = str(input("Please Enter an account number: "))
    if not username in user_dict:
        print("\nNot existing Account number")
        return False

    confirmation = input('Are you sure to delete {} account? (y/n): '.format(account_num))

    if confirmation == 'y' or confirmation == 'yes':
        user_dict.pop(account_num)
        write_user()
        print("Deletion Completed")
        return True
    elif confirmation == 'n' or confirmation == 'no':
        return False
    else:
        print("Invalid Input")
        return False


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

    while username != '' and password != '':
        if username in manage_account and password == manage_account[username]:
            print("Please select an option\n\n")
            print("1.Create an User Account  | 2.Delete existing User Account \n3.Report on User          | " \
                  + "4.Detail information of an Account \n5.open a new account        | 0.Exit\n\n")
            selection = input("Please Enter a Number above: ")
            while selection != '':
                if selection == '1':
                    create_account()
                    selection = '6'
                elif selection == '2':
                    delete_user()
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
    read_user()
    main(manager_account())