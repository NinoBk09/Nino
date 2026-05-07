import tkinter as tk

okno = tk.Tk()
okno.title("tic tac toe")

gumbi = []

for i in range(9):
    gumb = tk.Button(okno, text="", width="6", height="3")
    gumb.grid(row=i//3, column=i%3)
    gumbi.append(gumb)
    
okno.mainloop()
    