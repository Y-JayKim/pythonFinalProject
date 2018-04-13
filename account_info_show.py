import sys

sys.path.insert(0, './GUI/')
from tkinter import *

class AccountInfo:
    def __init__(self, parent,acc_type):
        self.master = parent
        # self.balance = balance
        self.master.title("Account Information Window")

        # Frames and its styles
        self.top_frame = Frame(self.master)
        self.accinfo_frame = Frame(self.master)
        self.acc_history_frame=Frame(self.master)

        self.top_frame.grid(row=0, sticky=W + E,pady=(0,10))
        self.accinfo_frame.grid(row=1,sticky=W + E,padx=(20,0),pady=(0,20))
        self.acc_history_frame.grid(row=2,sticky=W + E,padx=(20,0),pady=(0,20))

        self.back_button = Button(self.top_frame, text="<-", width=3, height=1)
        self.back_button.grid(row=0, column=0)

        self.balance_label = Label(self.top_frame, text="Account History")
        self.balance_label.grid(row=0, column=1, padx=(50, 0),pady=(10,0))
        # self.balance_show_label = Label(self.top_frame, text=self.balance)
        # self.balance_show_label.grid(row=0, column=2, pady=(10, 0))

        #-----------------------------------Account Info Display----------------------------------------------------
        self.account_type_show = Label(self.accinfo_frame, text="Account Type: ")
        self.account_type_show.grid(row=0)
        self.account_type=Label(self.accinfo_frame, text=acc_type)
        self.account_type.grid(row=0,column=1)

        #---------------------------------History Listbox---------------------------------------------------
        self.name_listbox = Listbox(self.acc_history_frame,height=10, width=20, selectmode=SINGLE)
        self.name_scrollbar = Scrollbar(self.acc_history_frame, orient='vertical')
        self.name_scrollbar.config(command=self.name_listbox.yview)
        self.name_listbox.config(yscrollcommand=self.name_scrollbar.set)
        self.name_listbox.pack(side=LEFT, fill=BOTH)
        self.name_scrollbar.pack(side=RIGHT, fill=Y)


if __name__ == '__main__':
    root = Tk()
    AccountInfo(root,"ACCOUNT")
    mainloop()