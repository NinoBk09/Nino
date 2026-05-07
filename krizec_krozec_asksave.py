import tkinter as tk
import json
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
from tkinter import messagebox

def klik(i):    
    global gumbi, igralec, seznam, d
    
    if gumbi[i]["text"] == "":
        seznam[i] = igralec
        gumbi[i]["text"] = seznam[i]
        print(seznam)
        
        if igralec == "X":
            igralec = "O"
        else:
            igralec = "X"
        d = {
                 'navrsti': igralec,
                 'stanje': seznam
            }
    izenaceno()        
    zmagovalec=zmaga()
    if zmagovalec:
        label.config(text=f"Zmaga {zmagovalec}", bg="lightgreen") 
        for g in gumbi:
            g.config(state="disable")

def zmaga():
    kombinacije = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for k in kombinacije:
        if gumbi[k[0]]["text"] == gumbi[k[1]]["text"] == gumbi[k[2]]["text"] != "":
            return gumbi[k[0]]["text"]
    return None

def reset():
    global igralec, seznam
    igralec = "X"
    label.config(text="")
    for gumb in gumbi:
        gumb.config(text="", state="normal")
    for i in range(len(seznam)-1,-1,-1):
        if seznam[i] != "":
            seznam[i] = ""
    print(seznam)
        
def izenaceno():
    global seznam
    if seznam.count("") == 0:
        label.config(text="Izenačeno", bg="yellow")
        for g in gumbi:
            g.config(state="disable")
            
def shrani():
    global d
    files = [('JSON dokument', '*.json'), ('Vse datoteke', '*.*')]
    file = asksaveasfile(filetypes=files, defaultextension=".json")
    json.dump(d,file)
    file.close()   
    label.config(text="Shranjeno", bg="lightgreen")

def nalozi():
    global d, igralec, seznam
    try:
        file = askopenfile(filetypes=[('JSON dokument', '*.json'), ('Vse datoteke', '*.*')])
        d = json.load(file)
        igralec = d['navrsti']
        seznam = d['stanje']   
        for i in range(9):
            gumbi[i].config(text=seznam[i],state="normal")
        
        label.config(text="datoteka uspešno naložena", bg="lightgreen")
    except FileNotFoundError:
        messagebox.showwarning("Error", "Datoteke nismo našli, nalagam novo.")
        d = {
                 'navrsti': igralec,
                 'stanje': seznam
            }
    except:
        messagebox.showwarning("Error", "Problme pri nalaganju datoteke.")
        
        
                   
okno = tk.Tk()
okno.title("polje")

messagebox.showerror("HAHA", "HAHA, ZLOBEN SEM IN DELAM NA ISTI DATOTEKI KOT TI!")

gumbi=[]
igralec = "X"
d=0
okvir_gumbi = tk.Frame(okno)
okvir_gumbi.pack(pady=10)

for i in range(9):
    gumb = tk.Button(okvir_gumbi, height=3, width=6, command=lambda i=i: klik(i))
    gumb.grid(row=i//3, column=i%3)
    gumbi.append(gumb)

okvir_spodaj = tk.Frame(okno)
okvir_spodaj.pack(pady=20)

gumb1 = tk.Button(okvir_spodaj, height=3, width=9,bg="lightblue", command=reset, text="Nova igra")
gumb1.grid(column=1, row=0)

gumb_shrani = tk.Button(okvir_spodaj, height=3, width=9,bg="darkblue", fg="white", command=shrani, text="Shrani" )
gumb_shrani.grid(column=2, row=0)

gumb_nalozi = tk.Button(okvir_spodaj, text="Naloži", height=3, width=9, bg="red", fg="white", command=nalozi)
gumb_nalozi.grid(column=3, row=0)

okvir_label = tk.Frame(okno)
okvir_label.pack(pady=10)

label = tk.Label(okvir_label, text="", pady="10")
label.grid(column=2, row=1)
seznam = ["","","","","","","","",""]
okno.mainloop()