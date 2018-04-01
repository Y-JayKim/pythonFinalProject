# management.py
#
# management CLI interface
#
# Yeonjae Kim   Minsu Song
#
import csv
from constant import *


def read_manager_account():
    manager = {}
    with open(MANAGER_ACCOUNT_FILE, 'r') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            manager[row[0]] = row[1]

    return manager


def check_user_exist(username):
    username_list = []
    with open(USER_ACCOUNT_FILE, 'r') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            username_list.append(row[0])
    if username in username_list:
        return False
    else:
        return True


def create_user():
    username = input("Please Enter a username: ")
    if not check_user_exist(username) or username == '':
        print("\nInvalid Input!!\n")
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
    pass


def report_on_users():
    pass


def account_detail():
    pass


def transaction():
    pass


def main(manage_account):
    print("--------------------------------------------------------------------\n")
    print("Hello, this program is for managing bank account\n")
    print("--------------------------------------------------------------------\n")
    print("Please Enter your username and password")
    username = input("Username:  ")
    password = input("Password:  ")

    while username != '' and password != '':
        if username in manage_account and password == manage_account[username]:
            print("Please select an option\n\n")
            print("1.Create an User Account  | 2.Delete a exist User Account \n3.Report on User          | " \
                  + "4.Detail information of an Account \n5.Transaction             | 0.Exit\n\n")
            selection = input("Please Enter a Number above: ")
            while selection != '':
                if selection == '1':
                    create_user()
                    selection = '6'
                elif selection == '2':
                    delete_user()
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
    main(read_manager_account())
