from tkinter import *
from tkinter import messagebox

class Help:
    def __init__(self, parent):
        self.master = parent
        self.master.title("Help Window")

        T = Text(self.master, height=10, width=50, padx=30, pady=20)
        T.pack()
        quote = """When you bank online, you’re not alone. In today’s world, online means more ways to connect than ever before. But it’s also about connecting to something bigger. It’s about getting answers when you need them and talking to people who’ve been there. So when you need help, we’re here to listen—along with an entire community of Capital One customers. Help is just a call, Café, or click away.
        
        Our number is 111-222-3333"""
        T.insert(END, quote)

if __name__ == '__main__':
    root = Tk()
    Help(root)
    mainloop()