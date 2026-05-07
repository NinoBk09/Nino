import tkinter as tk

okno = tk.Tk()
okno.title("aura")
x=0
label = tk.Label(okno, text=f"hej {x}")
label.pack()


def sestej():
    global x
    x+=6
    label.config(text=f"x = {x}")
gumb = tk.Button(okno, text="stisni me", command = sestej)
gumb.pack()

okno.mainloop()