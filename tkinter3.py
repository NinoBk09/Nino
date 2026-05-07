import tkinter as tk

okno = tk.Tk()
okno.title("števec")

x=0

def stevec():
    global x
    x+=3
    label.config(text=f"x = {x}")

label = tk.Label(okno, text="x = 0")
label.pack()

gumb = tk.Button(okno, text="sestej", command=stevec)
gumb.pack()

okno.mainloop()