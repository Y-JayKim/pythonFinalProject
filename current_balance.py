# current_balance.py
#
# current balance display when current balance and account button are clicked
#
# Yeonjae Kim  /  Minsu Song
#
from tkinter import *
from main_menu import MainMenu


class BalanceWindow(MainMenu):
    def __init__(self, parent):
        super().__init__(parent)
        self.balance = 10000

        self.master.title("Current Balance")

        # Frame
        self.top_frame = Frame(self.master)
        self.mid1_frame = Frame(self.master)
        self.mid2_frame = Frame(self.master)
        self.bottom_frame = Frame(self.master)

        self.top_frame.grid(row=0, padx=10, pady=10)
        self.mid1_frame.grid(row=1, padx=10, pady=30)
        self.mid2_frame.grid(row=2, padx=10, pady=30)
        self.bottom_frame.grid(row=3, padx=10, pady=10)

        # Widgets and Bind to Events
        self.balance_label = Label(self.top_frame, text="Current Balance:")
        self.balance_show_label = Label(self.top_frame, text=self.balance)

        self.input_label = Label(self.mid1_frame, text="Deposit/Withdraw Amount")
        self.dollar_label = Label(self.mid1_frame, text="$")
        self.input_entry = Entry(self.mid1_frame, width=20)

        self.number1_button = Button(self.mid2_frame, text="1")
        self.number2_button = Button(self.mid2_frame, text="2")
        self.number3_button = Button(self.mid2_frame, text="3")
        self.number4_button = Button(self.mid2_frame, text="4")
        self.number5_button = Button(self.mid2_frame, text="5")
        self.number6_button = Button(self.mid2_frame, text="6")
        self.number7_button = Button(self.mid2_frame, text="7")
        self.number8_button = Button(self.mid2_frame, text="8")
        self.number9_button = Button(self.mid2_frame, text="9")
        self.number0_button = Button(self.mid2_frame, text="0")

        self.confirm_button = Button(self.bottom_frame, text="Confirm")

        # Place Widgets On Window
        # Top
        self.balance_label.grid(row=0, column=0, padx=5, pady=0)
        self.balance_show_label.grid(row=0, column=1, padx=5, pady=0)

        # Mid 1
        self.input_label.grid(row=0, column=1, padx=5, pady=5)
        self.dollar_label.grid(row=1, column=0, sticky=E)
        self.input_entry.grid(row=1, column=1, padx=0, pady=5)

        # Mid 2
        self.number1_button.grid(row=0, column=0, padx=0, pady=0)
        self.number2_button.grid(row=0, column=1, padx=0, pady=0)
        self.number3_button.grid(row=0, column=2, padx=0, pady=0)
        self.number4_button.grid(row=1, column=0, padx=0, pady=0)
        self.number5_button.grid(row=1, column=1, padx=0, pady=0)
        self.number6_button.grid(row=1, column=2, padx=0, pady=0)
        self.number7_button.grid(row=2, column=0, padx=0, pady=0)
        self.number8_button.grid(row=2, column=1, padx=0, pady=0)
        self.number9_button.grid(row=2, column=2, padx=0, pady=0)
        self.number0_button.grid(row=3, column=1, padx=0, pady=0)

        # Bottom
        self.confirm_button.grid(row=1, column=1, padx=5, pady=5)


if __name__ == "__main__":
    root = Tk()
    BalanceWindow(root)
    mainloop()
