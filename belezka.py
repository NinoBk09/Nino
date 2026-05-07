import tkinter as tk
import json
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile

def note():
    global seznam
    
    a = vnos.get()
    if a:        
        seznam.append(a)
        print(seznam)
        label.config(text="\n".join(seznam))
        vnos.delete(0, 'end')
        
def save():
    global seznam
    files = [('JSON dokument', '*.json'), ('Vse datoteke', '*.*')]
    file = asksaveasfile(filetypes=files, defaultextension=".json")
    
    if file:
        json.dump(seznam, file)
        file.close
        print("shranjeno")
        
def load():
    global seznam
    try:
        files = [('JSON dokument', '*.json'), ('Vse datoteke', '*.*')]
        file = askopenfile(filetypes=files, defaultextension=".json")
        seznam = json.load(file)
        print("Uspešno naloženo")
        label.config(text="\n".join(seznam))
    except FileNotFoundError:
        print("Datoteka ni najdena, pripravljam novo: ")
        seznam=[]
    
    
        
seznam=[]
okno = tk.Tk()
okno.title("beležka")

zgornji_okvir = tk.Frame(okno)
zgornji_okvir.pack()

label = tk.Label(zgornji_okvir,text="", width=20, height=25, bg="white",justify="left",anchor="nw")
label.pack()

vnos = tk.Entry(zgornji_okvir, width=15)
vnos.pack()

spodnji_okvir = tk.Frame(okno)
spodnji_okvir.pack()

gumb= tk.Button(spodnji_okvir, text="v beležko", width=10, height=4, bg="darkred", fg="white", command=note)
gumb.pack(pady=5)

gumb_shrani = tk.Button(spodnji_okvir, text="save",width=10, height=4, bg="green",fg="white", pady=8, command=save)
gumb_shrani.pack()

gumb_nalozi = tk.Button(spodnji_okvir, text="load",width=10, height=4, bg="blue",fg="white", pady=8, command=load)
gumb_nalozi.pack()


okno.mainloop()