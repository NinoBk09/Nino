import tkinter as tk

okno = tk.Tk()
okno.title("gumba")
x=0
label = tk.Label(okno, text=f"x = {x}")
label.pack()

def sestej():
    global x
    x+=3
    label.config(text=f"x = {x}")

def restart():
    global x
    x = 0
    label.config(text=f"x = {x}")

gumb1 = tk.Button(okno, text="+3", command = sestej)
gumb1.pack()

gumb2 = tk.Button(okno, text="reset", command = restart)
gumb2.pack()

okno.mainloop()