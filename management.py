# management.py
#
# management CLI interface
#
# Yeonjae Kim   Minsu Song
#
import csv
from constant import *


def manager_account():
    manager = {}
    with open(MANAGER_ACCOUNT_FILE, 'r') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            manager[row[0]] = row[1]
    return manager

<<<<<<< HEAD

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
=======
def read_user_accounts():
    user_info={}
    with open(USER_ACCOUNT_FILE, 'r') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            user_info[row[0]] = row[1]
    return user_info


def check_user_exist(username):
    user_dict = read_user_accounts()
    if username in user_dict:
        return False
    else:
>>>>>>> c501d7055804b913fdca952d74ad024a19eab0d2
        return True
    else:
        return False


def check_user_password(username):
    user_dict = read_user_accounts()
    return user_dict.get(username)

def get_user_name_and_check(username):
    if not check_user_exist(username):
        print("\nThe Username already exists!!!\n")
        return False
    else:
        print("\nThe Username does not exist!!!\n")
        return False


def create_user():
    username = str(input("Please Enter a username: "))
<<<<<<< HEAD
    if user_name_check(username):
        print("User name is already exist!!")
        return False

=======
    if not check_user_exist(username):
        return False
    # get_user_name_and_check(username)
>>>>>>> c501d7055804b913fdca952d74ad024a19eab0d2
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
<<<<<<< HEAD
    username = str(input("Please Enter a username: "))
    if not user_name_check(username):
        print("The username is not exist")
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
=======
    user_name = str(input("Please Enter a username: "))
    # if check_user_exist(user_name):
    #     return False
    get_user_name_and_check(user_name)
    password = input("Please Enter password: ")
    password=str(password)
    existing_user_password = check_user_password(user_name)
    existing_user_password=str(existing_user_password)

    if existing_user_password == password:
        user_delete_confirm = input("Are you sure to delete your account? (y/n): ")
        user_delete_confirm=str(user_delete_confirm)
        if user_delete_confirm == 'y':
            user_dict = read_user_accounts()
            user_dict.pop(user_name)
            new_dict=user_dict
            with open(USER_ACCOUNT_FILE, 'w') as file:
                csv_file = csv.writer(file)
                for key in new_dict:
                    csv_file.writerow([key,new_dict[key]])
        elif user_delete_confirm == 'n':
            return False
    else:
        print("Invalid password")
        return False

>>>>>>> c501d7055804b913fdca952d74ad024a19eab0d2


def report_on_users():
    pass


def account_detail():
    pass


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
<<<<<<< HEAD
    main(manager_account())
=======
    main(read_manager_account())
>>>>>>> c501d7055804b913fdca952d74ad024a19eab0d2
