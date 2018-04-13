from teller_SelectionView import ManageSelection
from teller_LoginView import ManagementLogin
from model import *
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
    global model

    if sin not in user_dict:
        user_dict[sin] = []
        model.write_password(sin, '123')

    if not exist_account(account, sin):
        if account == 'chequing':
            user_dict[sin].append(Chequing(sin))
        elif account == 'saving':
            user_dict[sin].append(Saving(sin))
        elif account == 'term saving':
            user_dict[sin].append(TermSaving(sin))

        save_file()
    else:
        print('\nThe client already has {} account\n'.format(account))


#------------------ Deleting Account---------------------------------
def delete_account():
    sin = sin_check()

    if sin in user_dict:
        account_choice = input('Please enter account you want to delete:\t')
        for ind in range(len(user_dict[sin])):
            if account_choice == repr(user_dict[sin][ind]):
                user_dict[sin][ind].name = 000000000
                user_dict['000000000'].append(user_dict[sin][ind])
                user_dict[sin].pop(ind)
                save_file()
                return True

        print("There is no existing account")
    else:
        print('\nThe Client that matches with the SIN does not exist \n')


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
    global user_password

    username = input("Please enter the SIN:  ")
    if username in user_password:
        password = getpass.getpass("Current Password:  ")
        if password == user_password[username]:
            new_password = getpass.getpass('New Password:  ')
            new_password2 = getpass.getpass("Re-New Password:  ")
            if new_password == new_password2:
                model.write_password(username, new_password)
                print('\nPassword has been changed\n')
            else:
                print("\nPassword does not match\n")
        else:
            print('\nInvalid Password\n')
    else:
        print('\nThere is no {} in the list\n'.format(username))


def main():
    global model
    global manage_account

    first_page = ManagementLogin()
    first_page.asking_username()

    while first_page.username != '' and first_page.password != '':
        if first_page.username in manage_account and first_page.password == manage_account[first_page.username]:
            second_page = ManageSelection()
            second_page.selection_page()

            while second_page.selection != '':
                if second_page.selection == '1':
                    create()
                    second_page.selection = '5'
                elif second_page.selection == '2':
                    delete_account()
                    second_page.selection = '5'
                elif second_page.selection == '3':
                    show_transaction()
                    second_page.selection = '5'
                elif second_page.selection == '4':
                    change_password()
                    second_page.selection = '5'
                elif second_page.selection == '5':
                    second_page.selection_page()
                elif second_page.selection == '0' or second_page.selection == 'exit':
                    break
                else:
                    second_page.not_in_option()
                save_file()
            break
        else:
            first_page.wrong_password()

    print("\nThank you for using Management Program!")


if __name__ == '__main__':
    main()
