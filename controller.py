# login_page.py
#
# Log in window for Account.py
#
# Yeonjae Kim  /  Minsu Song
#
from tkinter import *
from tkinter import messagebox
from login_page import LoginWindow


def login_submit(event):
    if not LoginPage.username_entry.get():


def main():
    root = Tk()
    LoginPage = LoginWindow(root)
    global LoginPage
    LoginPage.submit_button.bind("<Button-1>", login_submit)
    mainloop()


if __name__ == '__main__':
    main()
