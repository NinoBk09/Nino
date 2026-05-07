import tkinter as tk
import json
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile

def modra():
    global c, d
    
    c = "blue"
    d = {
        'barva': c
        }
    okno.config(bg=d['barva'])
    
def rdeca():
    global c, d
    
    c = "red"
    d = {
        'barva': c
        }
    okno.config(bg=d['barva'])

def save():
    global d
    
    files = [('JSON dokument', '*.json'), ('Vse datoteke', '*.*')]
    file = asksaveasfile(filetypes=files, defaultextension=".json")
    if file:
        json.dump(d, file)
        file.close()
        print("uspešno shranjeno")

def load():
    global c, d
    
    try:
        files = [('JSON dokument', '*.json'), ('Vse datoteke', '*.*')]
        file = askopenfile(filetypes = files, defaultextension=".json")
        d = json.load(file)
        file.close()   
        print("uspešno naloženo")
        okno.config(bg=d['barva'])
        
    except FileNotFoundError:
        print("Datoteke ni bilo mogoče najti, nalagam novoo")
        d = {
            }
        
c = 0
d = 0
okno = tk.Tk()
okno.title("barvni_gumb")

gumb_modra = tk.Button(okno, text="modra", command=modra )
gumb_modra.pack()

gumb_rdeča = tk.Button(okno, text="rdeča", command=rdeca )
gumb_rdeča.pack()

gumb_shrani = tk.Button(okno, text="shrani", command=save)
gumb_shrani.pack()

gumb_nalozi = tk.Button(okno, text="load", command=load)
gumb_nalozi.pack()

okno.mainloop()