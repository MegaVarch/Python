from tkinter import *
from datetime import date

root = Tk()

root.title("Getting Started With Widgets")
root.geometry('400x300')

lbl = Label(text="Hey There!", fg = "white", bg = "#072F5F", height=1, width=100)

name_lbl = Label(text="Name", bg = "#389FD3")
name_entry = Entry()

def display():
    name = name_entry.get()
    global Message
    Message = "Welcome To the Application \nTodays date is: "
    greet = "Hello "+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, Message)
    text_box.insert(END, date.today())

text_box = Text(height = 3)

btn = Button(text="Begin!", command = display, bg = "#1261A0", height=1, fg = "white")

lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()






