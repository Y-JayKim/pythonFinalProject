# login_page.py
#
# Log in window for Account.py
#
# Yeonjae Kim  /  Minsu Song
#
from tkinter import *
from main_menu import MainMenu


class LoginWindow(MainMenu):
    def __init__(self, parent):
        super().__init__(parent)
        self.master.title("Login Window")

        # Checker
        self.submit_clicked = False

        # FRAME
        self.top_frame = Frame(self.master)
        self.mid_frame = Frame(self.master)
        self.bottom_frame = Frame(self.master)

        self.top_frame.grid(row=0, padx=30, pady=10)
        self.mid_frame.grid(row=1, padx=30, pady=10)
        self.bottom_frame.grid(row=3, padx=30, pady=10)

        # Widgets and Bind to Events
        self.login_label = Label(self.top_frame, text='LOG IN')

        self.username_label = Label(self.mid_frame, text='Username')
        self.username_entry = Entry(self.mid_frame, width=20)

        self.password_label = Label(self.mid_frame, text="Password")
        self.password_entry = Entry(self.mid_frame, show='*', width=20)

        self.submit_button = Button(self.bottom_frame, text="Submit")

        # Place Widgets On Window
        # Top
        self.login_label.grid(row=0, column=1, padx=5, pady=10)

        # Bottom
        self.username_label.grid(row=0, column=0, sticky=E, padx=5, pady=5)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        self.password_label.grid(row=1, column=0, sticky=E, padx=5, pady=5)
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        self.submit_button.grid(row=1, column=1, padx=5, pady=5)


if __name__ == "__main__":
    def hey(event):
        print("Hey!")
    root = Tk()
    L = LoginWindow(root)
    L.submit_button.bind("<Button-1>", hey)
    mainloop()
