import tkinter as tk

def klikni():
    label.config(text="stisnjen")

okno = tk.Tk()
okno.title("Moja prva aplikacija")


label= tk.Label(okno, text="Pozdravljen/a")
label.pack()

gumb= tk.Button(okno, text="stisni me", command=klikni)
gumb.pack()

print("znam uporabljati Github")
okno.mainloop()