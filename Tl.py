from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("Root Window")

def topwin():
    topwin = Toplevel()
    topwin.geometry("180x100")
    topwin.title("Toplevel Window")

    l2 = Label(topwin, text="This is Toplevel window")
    l2.pack()
    
    topwin.mainloop()

l2 = Label(root, text="This is a root window")
btn = Button(root, text="Click here to open another window", command = topwin)

l2.pack()
btn.pack()

root.mainloop


