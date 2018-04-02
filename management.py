# management.py
#
# management CLI interface
#
# Yeonjae Kim   Minsu Song
#
import csv
from constant import *
from account import *


def manager_account():
    manager = {}
    with open(MANAGER_ACCOUNT_FILE, 'r') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            manager[row[0]] = row[1]
    return manager


def read_user():
    user_dict = {}
    with open(USER_ACCOUNT_FILE, 'r') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            user_dict[row[0]] = row[1]
    return user_dict


def write_user(user_dict):
    with open(USER_ACCOUNT_FILE, 'w') as file:
        csv_file = csv.writer(file)
        for key in user_dict:
            csv_file.writerow([key, user_dict[key]])


def user_name_check(username):
    if username in read_user():
        return True
    else:
        return False


def create_user():
    username = str(input("Please Enter a username: "))
    if user_name_check(username):
        print("User name already exists!!")
        return False

    password = input("Please Enter password: ")
    password_confirm = input("Please re-enter the password: ")

    if password == password_confirm:
        print('username: {} and Password: {}\n'.format(username, password))
        print("Please type yes or y to continue.\nIf you want to cancel, please enter n or no\n")
        selection = input("---> :")
        if selection == 'y' or selection == 'yes':
            with open(USER_ACCOUNT_FILE, 'a') as file:
                csv_file = csv.writer(file)
                csv_file.writerow([username, password])
        elif selection == 'n' or selection == 'no':
            print("Okay ByeBye")


def delete_user():
    username = str(input("Please Enter a username: "))
    if not user_name_check(username):
        print("The username does not exist")
        return False

    confirmation = input('Are you sure to delete {} account? (y/n): '.format(username))

    if confirmation == 'y' or confirmation == 'yes':
        user_dict = read_user()
        user_dict.pop(username)
        write_user(user_dict)
        return True

    elif confirmation == 'n' or confirmation == 'no':
        return False

    else:
        print("Invalid Input")
        return False


def report_on_users():
    pass


def account_detail():
    """Shows account info such as account number, balance and name"""
    username = str(input("Please Enter a username: "))
    if not user_name_check(username):
        print("The username does not exist")
        return False

    password = input("Please Enter password: ")
    password_confirm = input("Please re-enter the password: ")

    #if password == password_confirm:


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
                  + "4.Detail information of an Account \n5.Transaction             | 0.Exit\n\n")
            selection = input("Please Enter a Number above: ")
            while selection != '':
                if selection == '1':
                    create_user()
                    selection = '6'
                elif selection == '2':
                    delete_user()
                    selection = '6'
                elif selection == '3':
                    report_on_users()
                elif selection == '4':
                    account_detail()
                elif selection == '5':
                    transaction()
                elif selection == '6':
                    print("1.Create an User Account  | 2.Delete a exist User Account \n3.Report on User          | "\
                          + "4.Detail information of an Account \n5.Transaction             | 0.Exit\n")
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
