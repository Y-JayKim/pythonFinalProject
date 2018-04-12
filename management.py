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


#------------------------Save and load file----------------------------
def save_file():
    global user_dict

    storage = Model(user_dict)
    storage.write_userinfo()
    # listoflist = []
    #
    # for key in user_dict:
    #     for value in user_dict[key]:
    #         listoflist.append([value.acc_num, repr(value), key, value.balance])
    # listoflist = sorted(listoflist, key=itemgetter(0))
    #
    # with open(USER_INFO_FILE, 'w') as file:
    #     fieldnames = ['acc_num', 'account', 'sin', 'balance']
    #     csv_writer = csv.writer(file)
    #
    #     csv_writer.writerow(fieldnames)
    #     for li in listoflist:
    #         csv_writer.writerow(li)


def load_file():
    global user_dict

    storage = Model(user_dict)
    storage.read_userinfo()
    # with open(USER_INFO_FILE, 'r') as csv_file:
    #     csv_reader = csv.reader(csv_file)
    #     next(csv_reader)
    #     for row in csv_reader:
    #         if not row == []:
    #             if row[2] not in user_dict:
    #                 user_dict[row[2]] = []
    #
    #             if row[1] == 'chequing':
    #                 user_dict[row[2]].append(Chequing(int(row[3])))
    #             elif row[1] == 'saving':
    #                 user_dict[row[2]].append(Saving(int(row[3])))
    #             elif row[1] == 'term saving':
    #                 user_dict[row[2]].append(TermSaving(int(row[3])))


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


#-------------------------------Main---------------------------------
def main(manage_account):
    load_file()

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
                  + "4. Show options again \n\t\t\t\t\t 0.Exit |\n\n")
            selection = input("Please Enter a Number above: ")
            while selection != '':
                if selection == '1':
                    create()
                    selection = '4'
                elif selection == '2':
                    delete_account()
                    selection = '4'
                elif selection == '3':
                    show_transaction()
                    selection = '4'
                elif selection == '4':
                    print("\n1.Create an User Account    | 2.Delete existing User Account \n" \
                          + "3.User's Transaction Report | 4. Show options again \n\t\t\t\t\t 0.Exit |\n\n")
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
    main(manager_account())
