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

        # FRAME
        self.top_frame = Frame(self.master)
        self.mid_frame = Frame(self.master)
        self.bottom_frame = Frame(self.master)
        self.right_frame = Frame(self.master)

        self.top_frame.grid(row=0, columnspan=2, padx=30)
        self.mid_frame.grid(row=1, padx=30)
        self.bottom_frame.grid(row=3, padx=30)
        self.right_frame.grid(row=1, column=1)

        # Widgets and Bind to Events
        self.login_label = Label(self.top_frame, text='SIGN IN', font=("Helvetica", 16))

        self.username_label = Label(self.mid_frame, text='Username')
        self.username_entry = Entry(self.mid_frame, width=20)

        self.password_label = Label(self.mid_frame, text="Password")
        self.password_entry = Entry(self.mid_frame, show='*', width=20)

        self.qr_image = PhotoImage(file="QR.png")
        self.qr_button = Button(self.right_frame, image=self.qr_image, width=70, height=70, cursor="hand2")
        self.qr_label = Label(self.right_frame, text="Sign In with QR code")

        self.submit_button = Button(self.bottom_frame, text="Submit")
        self.register_lost_label = Label(self.bottom_frame, text="lost username/password\nregister an username",\
                                         foreground='blue', cursor="hand2")
        # Place Widgets On Window
        # Top
        self.login_label.grid(row=0, column=2, pady=10)

        # Mid
        self.username_label.grid(row=0, column=1, sticky=E, padx=5, pady=5)
        self.username_entry.grid(row=0, column=2, padx=5, pady=5)

        self.password_label.grid(row=1, column=1, sticky=E, padx=5, pady=5)
        self.password_entry.grid(row=1, column=2, padx=5, pady=5)

        self.qr_button.grid(row=0, column=0)
        self.qr_label.grid(row=1, column=0)

        # Bottom
        self.submit_button.grid(row=1, column=2, padx=5, pady=5)
        self.register_lost_label.grid(row=2, column=2, sticky=E)


if __name__ == "__main__":
    def hey(event):
        print("Test Submit clicked")
    root = Tk()
    L = LoginWindow(root)
    L.submit_button.bind("<Button-1>", hey)
    mainloop()
