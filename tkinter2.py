import tkinter as tk

okno = tk.Tk()
okno.title("Dva gumba")

def gumb_ena():
    label.config(text="hi")
    
def gumb_dva():
    label.config(text="bye")
    
label= tk.Label(okno, text="stisni gumba")
label.pack()
    
gumb=tk.Button(okno, text="Stisni me", command=gumb_ena)
gumb.pack()

gumb=tk.Button(okno, text="Stisni me", command=gumb_dva)
gumb.pack()
okno.mainloop()