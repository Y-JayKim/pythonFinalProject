# login_page.py
#
# Log in window for Account.py
#
# Yeonjae Kim  /  Minsu Song
#
from tkinter import *
from tkinter import messagebox
from login_page import LoginWindow
from main_page import MainWindow
import csv
from constant import *


# global
<<<<<<< HEAD
user_dict = {}
=======
>>>>>>> c501d7055804b913fdca952d74ad024a19eab0d2
page = ''
root = Tk()


def user_account():
<<<<<<< HEAD
    global user_dict
=======
    user_dict ={}
>>>>>>> c501d7055804b913fdca952d74ad024a19eab0d2
    with open(USER_ACCOUNT_FILE, 'r') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            user_dict[row[0]] = row[1]


def login_submit(event):
    global page
    global root
<<<<<<< HEAD
    global user_dict
=======
>>>>>>> c501d7055804b913fdca952d74ad024a19eab0d2
    username = page.username_entry
    password = page.password_entry

    if username.get() in user_dict and user_dict[username.get()] == password.get():
        root2 = Tk()
        messagebox.showinfo("Sign In", "Log in Successfully")
<<<<<<< HEAD
        root.destroy()
=======
        page.master.destroy()
>>>>>>> c501d7055804b913fdca952d74ad024a19eab0d2
        page = MainWindow(root2)

    else:
        messagebox.showinfo("Invalid", "Invalid username/password")
        username.delete(0, "end")
        password.delete(0, "end")


def main():
    global page
    global root
<<<<<<< HEAD

    page = LoginWindow(root)

    page.submit_button.bind("<Button-1>", login_submit)
    page.password_entry.bind("<Return>", login_submit)
=======
    page = LoginWindow(root)

    page.submit_button.bind("<Button-1>", login_submit)
>>>>>>> c501d7055804b913fdca952d74ad024a19eab0d2

    mainloop()


if __name__ == '__main__':
    user_account()
    main()
