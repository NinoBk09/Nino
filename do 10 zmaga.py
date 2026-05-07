import tkinter as tk

okno = tk.Tk()
okno.title("igra")

x=0

label = tk.Label(okno, text=f"x = {x}")
label.pack()
    
def sestej():
    global x
    x+=1
    if x >= 10:
        label.config(text="ZMAGA")
    else:
        label.config(text=f"x = {x}")

gumb = tk.Button(okno, text="+1", command= sestej)
gumb.pack()

okno.mainloop()