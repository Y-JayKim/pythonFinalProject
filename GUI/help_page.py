import sys
sys.path.insert(0, './GUI/')
from tkinter import *
from main_menu import MainMenu

class Help:
    def __init__(self, parent):
        self.master = parent
        self.master.title("Help Window")

        # Frames and its styles
        self.top_frame = Frame(self.master)
        self.text_frame = Frame(self.master)
        self.top_frame.grid(row=0, sticky=W+E)
        self.text_frame.grid(row=1)

        self.back_button = Button(self.top_frame, text="<-", width=3, height=1)
        self.back_button.grid(row=0, column=0)

        self.help_label = Label(self.top_frame, text="Help Page")
        self.help_label.grid(row=0, column=1, padx=(140, 0))

        T = Text(self.text_frame, height=10, width=50, padx=30, pady=40)
        T.pack()
        quote = """When you bank online, you’re not alone. In today’s world, online means more ways to connect than ever before. But it’s also about connecting to something bigger. It’s about getting answers when you need them and talking to people who’ve been there. So when you need help, we’re here to listen—along with an entire community of Capital One customers. Help is just a call, Café, or click away.
        
        Our number is 111-222-3333"""
        T.insert(END, quote)

if __name__ == '__main__':
    root = Tk()
    Help(root)
    mainloop()