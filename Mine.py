from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x300")

def msg():
    messagebox.showwarning("Hello", "Whats Up")

def hello(event):
    print("Hello! Event Triggered")

root.bind("<Return>", hello)

button = Button(root, text = "Hello, hope you have a nice day",command=msg)
button.place(x=40, y=80)

root.mainloop()