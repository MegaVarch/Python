from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# -------------------------------
# Setting up Main Window
# -------------------------------
root = Tk()
root.title("Denomination Counter")
root.configure(bg="light blue")
root.geometry("650x400")

# -------------------------------
# Adding Image and Labels in Main Window
# -------------------------------
upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg="light blue")
label.place(x=180, y=20)

label1 = Label(
    root,
    text="Hey User! Welcome to Denomination Counter Application.",
    bg="light blue"
)
label1.place(relx=0.5, y=340, anchor=CENTER)

# -------------------------------
# Function to open messagebox
# -------------------------------
def msg():
    MsgBox = messagebox.showinfo(
        "Alert",
        "Do you want to calculate the denomination count?"
    )
    if MsgBox == "ok":
        topwin()

# -------------------------------
# Adding Button in Main Window
# -------------------------------
button1 = Button(
    root,
    text="Let's get started!",
    command=msg,
    bg="brown",
    fg="white"
)
button1.place(x=260, y=360)

# -------------------------------
# Function for opening new/top window
# -------------------------------
def topwin():
    top = Toplevel()
    topwin.geometry("600x350+50+50")
    topwin.configure(bg="light grey")
    topwin.title("Calculator")

    label = Label(topwin, text="Enter total amount", bg="light grey")
    entry=Entry(topwin)
    lbl = Label(topwin, text="Here are the number of notes for each denomination", bg="light grey")

    l1 = Label(top, text="2000", bg="light grey")
    l2 = Label(top, text="500", bg="light grey")
    l3 = Label(top, text="100", bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

def calculator():
    try:
        amount = int(Entry.get())

        note2000 = amount // 2000
        amount %= 2000

        note500 = amount // 500
        amount %= 500

        note100 = amount // 100

    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)

    t1.insert(END, str(note2000))
    t2.insert(END, str(note500))
    t3.insert(END, str(note100))

    except ValueError:
        messagebox.showerror("Error", "Please enter a Valid number")

btn = Button(top, text="Calculate")
    




    
    

      


        
        



