import tkinter as tk
import json
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
from tkinter import messagebox

def klik(i):    
    global gumbi, igralec, seznam, d, player1, player2, izenaceno
    
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
                 'stanje': seznam,
                 'zmaga_X': player1,
                 'zmaga_y': player2,
                 'izenaceno': dif
            }
    izenaceno()        
    zmagovalec=zmaga()
    if zmagovalec:
        label.config(text=f"Zmaga {zmagovalec}", fg="lightgreen") 
        for g in gumbi:
            g.config(state="disable")

def zmaga():
    global player1, player2
    kombinacije = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for k in kombinacije:
        if gumbi[k[0]]["text"] == gumbi[k[1]]["text"] == gumbi[k[2]]["text"] != "":
            if igralec == "O":
                player1 += 1
                d['zmaga_x'] = player1
                label_x.config(text=f"X zmage: {player1}")
            elif igralec == "X":
                player2 += 1
                d['zmaga_y'] = player2
                label_o.config(text=f"O zmage: {player2}")
            return gumbi[k[0]]["text"]
    return None

def reset():
    global igralec, seznam, zacetek
    
    zacetek += 1
    if zacetek%2 == 1:
        igralec = "O"
        label_zacetek.config(text=f"Začne: {igralec}")        
    else:
        igralec = "X"
        label_zacetek.config(text=f"Začne: {igralec}") 
    label.config(text="")
    for gumb in gumbi:
        gumb.config(text="", state="normal")
    for i in range(len(seznam)-1,-1,-1):
        if seznam[i] != "":
            seznam[i] = ""
    print(seznam)
    label.config(bg="#f0f0f0")
    
        
def izenaceno():
    global seznam, dif, d
    if seznam.count("") == 0:
        dif += 1
        d['izenaceno'] = dif
        label_izenaceno.config(text=f"izenačeno: {dif}")
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
    global d, igralec, seznam, dif, player2, player1
    try:
        file = askopenfile(filetypes=[('JSON dokument', '*.json'), ('Vse datoteke', '*.*')])
        d = json.load(file)
        igralec = d['navrsti']
        seznam = d['stanje']
        if not zmaga:
            for i in range(9):
                gumbi[i].config(text=seznam[i],state="normal")
        label_izenaceno.config(text=f"izenačeno: {d['izenaceno']}")
        label_o.config(text=f"O zmage: {d['zmaga_y']}")
        label_x.config(text=f"X zmage: {d['zmaga_x']}")
        player1 = d['zmaga_x']
        player2 = d['zmaga_y']
        dif = d['izenaceno']
        
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
okno.configure(bg="#f0f0f0")

zacetek = 0
player1 = 0
player2 = 0
dif = 0
gumbi=[]
igralec = "X"
d=0

label_zacetek = tk.Label(okno, text=f"Začne: {igralec}", height=3, width=9, font=("Arial", 15, "bold"), bg="#E6E6E6",relief="flat")
label_zacetek.pack()

okvir_gumbi = tk.Frame(okno)
okvir_gumbi.pack(pady=10)

for i in range(9):
    gumb = tk.Button(okvir_gumbi, height=3, width=6, command=lambda i=i: klik(i), bg="#cccccc", font=("Arial", 15, "bold"))
    gumb.grid(row=i//3, column=i%3,)
    gumbi.append(gumb)

okvir_spodaj = tk.Frame(okno)
okvir_spodaj.pack(pady=20)

gumb1 = tk.Button(okvir_spodaj, height=3, width=9,bg="#687982", command=reset, text="Nova igra", fg="white",  relief="flat", bd=0, highlightthickness=0,font=("Helvetica", 10, "bold"))
gumb1.grid(column=1, row=0, padx=5)

gumb_shrani = tk.Button(okvir_spodaj, height=3, width=9,bg="#688271", fg="white", command=shrani, text="Shrani", relief="flat", bd=0, font=("Helvetica", 10, "bold"), highlightthickness=0)
gumb_shrani.grid(column=2, row=0, padx=5)

gumb_nalozi = tk.Button(okvir_spodaj, text="Naloži", height=3, width=9, bg="#716882", fg="white", command=nalozi, relief="flat", bd=0, font=("Helvetica", 10, "bold"), highlightthickness=0)
gumb_nalozi.grid(column=3, row=0, padx=5)

okvir_label = tk.Frame(okno)
okvir_label.pack(pady=10,)

label = tk.Label(okvir_label, text="", pady="10",font=("Helvetica", 14, "bold"))
label.grid(column=2, row=1)

okvir_rezultat = tk.Frame(okno)
okvir_rezultat.pack()

label_x = tk.Label(okvir_rezultat, text=f"X zmage: {player1}", height=3, width=9, font="Segoe_UI",)
label_x.grid(row=0,column=0, sticky="w")

label_o = tk.Label(okvir_rezultat, text=f"O zmage: {player2}", height=3, width=9, font="Segoe_UI")
label_o.grid(row=1,column=0, sticky="w")

label_izenaceno = tk.Label(okvir_rezultat, text=f"izenačeno: {dif}", height=3, width=9, font="Segoe_UI")
label_izenaceno.grid(row=2,column=0, sticky="w")

seznam = ["","","","","","","","",""]
okno.mainloop()