
from tkinter import *

# STEP 1: Create the Main Window

root = Tk()
root.title("ATM PIN Setup Interface")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#EAF4FC")


# STEP 2: Create the Details Frame

details_frame = Frame(
    root,
    width=360,
    height=160,
    bg="#072F5F"
)
details_frame.place(x=20, y=20)


# STEP 3: Add Labels and Entry Widgets

lbl = Label(
    details_frame,
    text="ATM PIN SETUP",
    fg="white",
    bg="#072F5F",
    font=("Arial", 14, "bold")
)
lbl.place(x=100, y=5)

Accname_lbl = Label(
    details_frame,
    text="Account Name",
    bg="#072F5F",
    fg="white"
)
Accname_lbl.place(x=15, y=45)

Accname_entry = Entry(details_frame, width=25)
Accname_entry.place(x=130, y=45)

pin_lbl = Label(
    details_frame,
    text="Enter PIN",
    bg="#072F5F",
    fg="white"
)
pin_lbl.place(x=15, y=80)

pin_entry = Entry(
    details_frame,
    show="*",
    width=25
)
pin_entry.place(x=130, y=80)


# STEP 4: Create the Button Function

def confirm_pin():
    name = Accname_entry.get().strip()
    val = pin_entry.get()

    message_box.delete("1.0", END)

    if name == "":
        message_box.insert(END, "Please enter your account name.")

    elif val == "":
        message_box.insert(END, "Please enter your PIN.")

    elif len(val) != 4 or not val.isdigit():
        message_box.insert(END, "PIN must contain 4 digits.")

    else:
        message_box.insert(END, "ATM PIN setup successful!")


# STEP 5: Create a Bordered Keypad Frame

keypad_frame = Frame(
    root,
    relief=SUNKEN,
    borderwidth=2,
    bg="#D0EFFF"
)
keypad_frame.place(x=80, y=195, width=240, height=155)


# STEP 6: Prepare the Keypad Values

nums = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1],
    ["#", 0, "*"]
]


# STEP 7: Build the Grid of Cells

for i in range(4):
    for j in range(3):

        frame = Frame(
            keypad_frame,
            relief=RAISED,
            borderwidth=2,
            bg="#D0EFFF",
            width=70,
            height=30
        )

        frame.grid(
            row=i,
            column=j,
            padx=5,
            pady=3
        )

        frame.grid_propagate(False)

        label = Label(
            frame,
            text=nums[i][j],
            bg="#D0EFFF",
            font=("Arial", 11, "bold")
        )

        label.place(relx=0.5, rely=0.5, anchor=CENTER)


# STEP 8: Add the Button and Message Box

confirm_button = Button(
    root,
    text="Set ATM PIN",
    command=confirm_pin,
    bg="#389FD3",
    fg="white",
    font=("Arial", 11, "bold")
)

confirm_button.place(
    x=125,
    y=365,
    width=150,
    height=35
)

message_box = Text(
    root,
    width=40,
    height=2,
    font=("Arial", 10),
    wrap=WORD
)

message_box.place(
    x=30,
    y=415,
    width=340,
    height=55
)


# STEP 9: Widgets positioned using place()
# Keypad cells are arranged using grid().


# STEP 10: Run and Test the Application

root.mainloop()

