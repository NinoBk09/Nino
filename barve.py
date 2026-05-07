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
    
    with open('file.json', 'w') as s:
        json.dump(d,s)
    print("uspešno shranjeno")

def load():
    global c, d
    
    try:
        with open('file.json', 'r') as s:
            d = json.load(s)
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