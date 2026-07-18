from tkinter import *
import random

root = Tk()
root.title("HydroGrid Dashboard")
root.geometry("900x600")
root.configure(bg="white")

canvas = Canvas(root, width=900, height=600, bg="white")
canvas.pack()

# ---------- Title ----------
canvas.create_text(
    450, 30,
    text="💧 HydroGrid Smart Water Management",
    font=("Arial", 22, "bold"),
    fill="darkblue"
)

# ---------- Live Values ----------
humidity_text = canvas.create_text(
    120, 80,
    text="Humidity: 70%",
    font=("Arial", 14, "bold"),
    fill="green"
)

solar_text = canvas.create_text(
    420, 80,
    text="Solar: 90%",
    font=("Arial", 14, "bold"),
    fill="orange"
)

tank_text = canvas.create_text(
    720, 80,
    text="Tank: 0%",
    font=("Arial", 14, "bold"),
    fill="blue"
)

# ---------- Clouds ----------
canvas.create_oval(60,120,140,170,fill="lightgray",outline="")
canvas.create_oval(100,100,180,170,fill="lightgray",outline="")

# ---------- Rain ----------
raindrops = []

for i in range(20):
    x = random.randint(80,170)
    drop = canvas.create_line(x,170,x,185,fill="blue",width=2)
    raindrops.append(drop)

# ---------- Tank ----------
canvas.create_rectangle(320,170,520,450,width=3)

water = canvas.create_rectangle(
    322,448,
    518,448,
    fill="deepskyblue",
    outline=""
)

canvas.create_text(
    420,155,
    text="Storage Tank",
    font=("Arial",13,"bold")
)

# ---------- Pipe ----------
canvas.create_line(520,310,700,310,width=10,fill="gray")

flow = []

for i in range(8):
    circle = canvas.create_oval(
        520+i*20,
        300,
        530+i*20,
        310,
        fill="deepskyblue",
        outline=""
    )
    flow.append(circle)

# ---------- House ----------
canvas.create_rectangle(720,240,820,360,fill="bisque")

canvas.create_polygon(
    715,240,
    770,190,
    825,240,
    fill="brown"
)

house_status = canvas.create_text(
    770,
    390,
    text="Waiting...",
    font=("Arial",13,"bold"),
    fill="red"
)

level = 0

def animate():

    global level

    # Rain animation
    for d in raindrops:
        canvas.move(d,0,10)
        x1,y1,x2,y2 = canvas.coords(d)

        if y2>170:
            newx=random.randint(80,170)
            canvas.coords(d,newx,170,newx,185)

    # Tank filling
    if level<100:
        level+=1

    top = 448-(level*2.7)

    canvas.coords(
        water,
        322,
        top,
        518,
        448
    )

    canvas.itemconfig(
        tank_text,
        text=f"Tank: {level}%"
    )

    canvas.itemconfig(
        humidity_text,
        text=f"Humidity: {random.randint(60,90)}%"
    )

    canvas.itemconfig(
        solar_text,
        text=f"Solar: {random.randint(85,100)}%"
    )

    # Water flowing through pipe
    if level>40:

        for c in flow:

            canvas.move(c,8,0)

            x1,y1,x2,y2=canvas.coords(c)

            if x1>700:
                canvas.coords(c,520,300,530,310)

    # House gets water
    if level==100:
        canvas.itemconfig(
            house_status,
            text="✅ Water Supplied",
            fill="green"
        )

    root.after(80,animate)

animate()

root.mainloop()