import tkinter as tk
import json
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import random

def izbira_O():
    global seznam
    nasprotnik = ""
    dvavrsta_0 = [[3,6],[4,8],[1,2]]
    dvavrsta_1 = [[0,2],[4,7]]
    dvavrsta_2 = [[4,6],[5,8],[0,1]]
    dvavrsta_3 = [[0,6],[4,5]]
    dvavrsta_4 = [[1,7],[3,5],[0,8],[2,6]]
    dvavrsta_5 = [[3,4],[2,8]]
    dvavrsta_6 = [[0,3],[2,4],[7,8]]
    dvavrsta_7 = [[1,4],[6,8]]
    dvavrsta_8 = [[6,7],[0,4],[2,5]]

#preveri blokado
    for i in dvavrsta_0:
        if seznam[i[0]] == seznam[i[1]] == "X":
            nasprotnik = 0
            if seznam[nasprotnik] == "":    
                return nasprotnik
#preveri zmago             
    for i in dvavrsta_0:
        if seznam[i[0]] == seznam[i[1]] == "O":
            nasprotnik = 0
            if seznam[nasprotnik] == "":    
                return nasprotnik
#preveri blokado
    for i in dvavrsta_1:
        if seznam[i[0]] == seznam[i[1]] == "X":
            nasprotnik = 1
            if seznam[nasprotnik] == "":    
                return nasprotnik
#preveri zmago
    for i in dvavrsta_1:
        if seznam[i[0]] == seznam[i[1]] == "O":
            nasprotnik = 1
            if seznam[nasprotnik] == "":    
                return nasprotnik
#preveri blokado
    for i in dvavrsta_2:
        if seznam[i[0]] == seznam[i[1]] == "X":
            nasprotnik = 2
            if seznam[nasprotnik] == "":    
                return nasprotnik
#preveri zmago
    for i in dvavrsta_2:
        if seznam[i[0]] == seznam[i[1]] == "O":
            nasprotnik = 2
            if seznam[nasprotnik] == "":    
                return nasprotnik            
#preveri blokado            
    for i in dvavrsta_3:
        if seznam[i[0]] == seznam[i[1]] == "X":
            nasprotnik = 3
            if seznam[nasprotnik] == "":    
                return nasprotnik
#preveri zmago
    for i in dvavrsta_3:
        if seznam[i[0]] == seznam[i[1]] == "O":
            nasprotnik = 3
            if seznam[nasprotnik] == "":    
                return nasprotnik
#preveri blokado
    for i in dvavrsta_4:
        if seznam[i[0]] == seznam[i[1]] == "X":
            nasprotnik = 4
            if seznam[nasprotnik] == "":    
                return nasprotnik
#preveri zmago
    for i in dvavrsta_4:
        if seznam[i[0]] == seznam[i[1]] == "O":
            nasprotnik = 4
            if seznam[nasprotnik] == "":    
                return nasprotnik
#preveri blokado
    for i in dvavrsta_5:
        if seznam[i[0]] == seznam[i[1]] == "X":
            nasprotnik = 5
            if seznam[nasprotnik] == "":    
                return nasprotnik
#preveri zmago
    for i in dvavrsta_5:
        if seznam[i[0]] == seznam[i[1]] == "O":
            nasprotnik = 5
            if seznam[nasprotnik] == "":    
                return nasprotnik
#preveri blokado
    for i in dvavrsta_6:
        if seznam[i[0]] == seznam[i[1]] == "X":
            nasprotnik = 6
            if seznam[nasprotnik] == "":    
                return nasprotnik
#preveri zmago
    for i in dvavrsta_6:
        if seznam[i[0]] == seznam[i[1]] == "O":
            nasprotnik = 6
            if seznam[nasprotnik] == "":    
                return nasprotnik
#preveri blokado
    for i in dvavrsta_7:
        if seznam[i[0]] == seznam[i[1]] == "X":
            nasprotnik = 7
            if seznam[nasprotnik] == "":    
                return nasprotnik
#preveri zmago

    for i in dvavrsta_7:
        if seznam[i[0]] == seznam[i[1]] == "O":
            nasprotnik = 7
            if seznam[nasprotnik] == "":    
                return nasprotnik
#preveri blokado
    for i in dvavrsta_8:
        if seznam[i[0]] == seznam[i[1]] == "X":
            nasprotnik = 8
            if seznam[nasprotnik] == "":    
                return nasprotnik
#preveri zmago
    for i in dvavrsta_8:
        if seznam[i[0]] == seznam[i[1]] == "O":
            nasprotnik = 8
            if seznam[nasprotnik] == "":    
                return nasprotnik
    while True:
        nasprotnik = random.randint(0,8)
        if gumbi[nasprotnik]['text'] == '':
            return nasprotnik
        
            

def klik(i):    
    global gumbi, igralec, seznam, d, player1, player2, izenaceno, H, vrsta
    stop = ""
    if vrsta%2 == 0:
        vrsta += 1
        if gumbi[i]["text"] == "":
            seznam[i] = igralec
            gumbi[i]["text"] = seznam[i]
            stop = izenaceno()
            if stop == "JA":
                return None
            if stop == "KONEC":
                zmagovalec=zmaga()
                if zmagovalec:
                    label.config(text=f"Zmaga {zmagovalec}", fg="lightgreen") 
                    for g in gumbi:
                        g.config(state="disable")
                return
    if vrsta%2 == 1:
        vrsta += 1
        nasprotnik = izbira_O()
        seznam[nasprotnik] = "O"
        gumbi[nasprotnik]["text"] = seznam[nasprotnik]
        
        stop = izenaceno()
        if stop == "JA":
            return None

        
        print(seznam)
        zmagovalec=zmaga()
        if zmagovalec:
            label.config(text=f"Zmaga {zmagovalec}", fg="lightgreen") 
            for g in gumbi:
                g.config(state="disable")

# h za X 
        if i == 0:
            if seznam[1] == "X" or seznam[1] == "":
                if seznam[2] == "X" or seznam[2] == "":
                    H+=1
            if seznam[4] == "X" or seznam[4] == "":
                if seznam[8] == "X" or seznam[8] == "":
                    H+=1
            if seznam[3] == "X" or seznam[3] == "":
                if seznam[6] == "X" or seznam[6] == "":
                    H+=1           
        if i == 1:
            if seznam[0] == "X" or seznam[0] == "":
                if seznam[2] == "X" or seznam[2] == "":
                    H+=1
            if seznam[4] == "X" or seznam[4] == "":
                if seznam[7] == "X" or seznam[7] == "":
                    H+=1       
        if i == 2:
            if seznam[1] == "X" or seznam[1] == "":
                if seznam[0] == "X" or seznam[0] == "":
                    H+=1
            if seznam[4] == "X" or seznam[4] == "":
                if seznam[6] == "X" or seznam[6] == "":
                    H+=1
            if seznam[5] == "X" or seznam[5] == "":
                if seznam[8] == "X" or seznam[8] == "":
                    H+=1  
        if i == 3:
            if seznam[0] == "X" or seznam[0] == "":
                if seznam[6] == "X" or seznam[6] == "":
                    H+=1
            if seznam[4] == "X" or seznam[4] == "":
                if seznam[5] == "X" or seznam[5] == "":
                    H+=1  
        if i == 4:
            if seznam[0] == "X" or seznam[0] == "":
                if seznam[8] == "X" or seznam[8] == "":
                    H+=1
            if seznam[1] == "X" or seznam[1] == "":
                if seznam[7] == "X" or seznam[7] == "":
                    H+=1
            if seznam[2] == "X" or seznam[2] == "":
                if seznam[6] == "X" or seznam[6] == "":
                    H+=1
            if seznam[3] == "X" or seznam[3] == "":
                if seznam[5] == "X" or seznam[5] == "":
                    H+=1
        if i == 5:
            if seznam[2] == "X" or seznam[2] == "":
                if seznam[8] == "X" or seznam[8] == "":
                    H+=1
            if seznam[3] == "X" or seznam[3] == "":
                if seznam[5] == "X" or seznam[5] == "":
                    H+=1
        if i == 6:
            if seznam[0] == "X" or seznam[0] == "":
                if seznam[3] == "X" or seznam[3] == "":
                    H+=1
            if seznam[4] == "X" or seznam[4] == "":
                if seznam[2] == "X" or seznam[2] == "":
                    H+=1
            if seznam[7] == "X" or seznam[7] == "":
                if seznam[8] == "X" or seznam[8] == "":
                    H+=1
        if i == 7:
            if seznam[6] == "X" or seznam[6] == "":
                if seznam[8] == "X" or seznam[8] == "":
                    H+=1
            if seznam[1] == "X" or seznam[1] == "":
                if seznam[4] == "X" or seznam[4] == "":
                    H+=1
        if i == 8:
            if seznam[2] == "X" or seznam[2] == "":
                if seznam[5] == "X" or seznam[5] == "":
                    H+=1
            if seznam[4] == "X" or seznam[4] == "":
                if seznam[0] == "X" or seznam[0] == "":
                    H+=1
            if seznam[7] == "X" or seznam[7] == "":
                if seznam[6] == "X" or seznam[6] == "":
                    H+=1
# h za O
        if  nasprotnik == 1:
            if seznam[0] == "O" or seznam[0] == "":
                if seznam[2] == "O" or seznam[2] == "":
                    H-=1
            if seznam[4] == "O" or seznam[4] == "":
                if seznam[7] == "O" or seznam[7] == "":
                    H-=1       
        if nasprotnik == 2:
            if seznam[1] == "O" or seznam[1] == "":
                if seznam[0] == "O" or seznam[0] == "":
                    H-=1
            if seznam[4] == "O" or seznam[4] == "":
                if seznam[6] == "O" or seznam[6] == "":
                    H-=1
            if seznam[5] == "O" or seznam[5] == "":
                if seznam[8] == "O" or seznam[8] == "":
                    H-=1  
        if nasprotnik == 3:
            if seznam[0] == "O" or seznam[0] == "":
                if seznam[6] == "O" or seznam[6] == "":
                    H-=1
            if seznam[4] == "O" or seznam[4] == "":
                if seznam[5] == "O" or seznam[5] == "":
                    H-=1  
        if nasprotnik == 4:
            if seznam[0] == "O" or seznam[0] == "":
                if seznam[8] == "O" or seznam[8] == "":
                    H-=1
            if seznam[1] == "O" or seznam[1] == "":
                if seznam[7] == "O" or seznam[7] == "":
                    H-=1
            if seznam[2] == "O" or seznam[2] == "":
                if seznam[6] == "O" or seznam[6] == "":
                    H-=1
            if seznam[3] == "O" or seznam[3] == "":
                if seznam[5] == "O" or seznam[5] == "":
                    H-=1
        if nasprotnik == 5:
            if seznam[2] == "O" or seznam[2] == "":
                if seznam[8] == "O" or seznam[8] == "":
                    H-=1
            if seznam[3] == "O" or seznam[3] == "":
                if seznam[5] == "O" or seznam[5] == "":
                    H-=1
        if nasprotnik == 6:
            if seznam[0] == "O" or seznam[0] == "":
                if seznam[3] == "O" or seznam[3] == "":
                    H-=1
            if seznam[4] == "O" or seznam[4] == "":
                if seznam[2] == "O" or seznam[2] == "":
                    H-=1
            if seznam[7] == "O" or seznam[7] == "":
                if seznam[8] == "O" or seznam[8] == "":
                    H-=1
        if nasprotnik == 7:
            if seznam[6] == "O" or seznam[6] == "":
                if seznam[8] == "O" or seznam[8] == "":
                    H-=1
            if seznam[1] == "O" or seznam[1] == "":
                if seznam[4] == "O" or seznam[4] == "":
                    H-=1
        if nasprotnik == 8:
            if seznam[2] == "O" or seznam[2] == "":
                if seznam[5] == "O" or seznam[5] == "":
                    H-=1
            if seznam[4] == "O" or seznam[4] == "":
                if seznam[0] == "O" or seznam[0] == "":
                    H-=1
            if seznam[7] == "O" or seznam[7] == "":
                if seznam[6] == "O" or seznam[6] == "":
                    H-=1
        print(f"h je {H}")
    
    d = {
                 'stanje': seznam,
                 'zmaga_X': player1,
                 'zmaga_y': player2,
                 'izenaceno': dif,
                 'H': H
            }
              
        
def zmaga():
    global gumbi, player1, player2
    kombinacije = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for k in kombinacije:
        if gumbi[k[0]]["text"] == "X" and gumbi[k[1]]["text"] == "X" and gumbi[k[2]]["text"] == "X":
            player1 += 1
            d['zmaga_x'] = player1
            label_x.config(text=f"X zmage: {player1}")
            return "X"
    for k in kombinacije:
        if gumbi[k[0]]["text"] == "O" and gumbi[k[1]]["text"] == "O" and gumbi[k[2]]["text"] == "O":
            player2 += 1
            d['zmaga_y'] = player2
            label_o.config(text=f"O zmage: {player2}")
            return "O"
    return None
        
    

def reset():
    global igralec, seznam, H, restart, vrsta
    if restart %2 == 0:
        zacne = "O"
        vrsta = 1
    else:
        zacne = "X"
        vrsta = 2
    restart+=1
    label_zacetek.config(text=f"Začne: {zacne}") 
    label.config(text="")
    for gumb in gumbi:
        gumb.config(text="", state="normal")
    for i in range(len(seznam)-1,-1,-1):
        if seznam[i] != "":
            seznam[i] = ""
    print(seznam)
    label.config(bg="#f0f0f0")
    H = 0
    
        
def izenaceno():
    global seznam, dif, d, player1, vrsta
    if seznam.count("") == 0:
        z = zmaga()
        if z == "X" or z =="O":
            player1 -= 1
            return "KONEC"
        else:
            dif += 1
            d['izenaceno'] = dif
            label_izenaceno.config(text=f"izenačeno: {dif}")
            label.config(text="Izenačeno", bg="yellow")
            for g in gumbi:
                g.config(state="disable")
            return "JA"
            
def shrani():
    global d
    
    d = {
        'stanje': seznam,
        'zmaga_x': player1,
        'zmaga_y': player2,
        'izenaceno': dif,
        'H': H
        }
    
    files = [('JSON dokument', '*.json'), ('Vse datoteke', '*.*')]
    file = asksaveasfile(filetypes=files, defaultextension=".json")
    json.dump(d,file)
    file.close()   
    label.config(text="Shranjeno", bg="lightgreen")

def nalozi():
    global d, seznam, dif, player2, player1, H
    file = askopenfile(filetypes=[('JSON dokument', '*.json'), ('Vse datoteke', '*.*')])
    if file:
        try: 
            d = json.load(file)
            seznam = d['stanje']
            for i in range(9):
                    gumbi[i].config(text=seznam[i],state="normal")
            z = zmaga()
            if z == "X" or z == "O":
                seznam = ["","","","","","","","",""]
                for i in range(9):
                    gumbi[i].config(text=seznam[i],state="normal")
            label_izenaceno.config(text=f"izenačeno: {d['izenaceno']}")
            label_o.config(text=f"O zmage: {d['zmaga_y']}")
            label_x.config(text=f"X zmage: {d['zmaga_x']}")
            player1 = d['zmaga_x']
            player2 = d['zmaga_y']
            dif = d['izenaceno']
            H = d['H'] 
            label.config(text="datoteka uspešno naložena", bg="lightgreen", fg="white")
            file.close()
        except FileNotFoundError:
            messagebox.showwarning("Error", "Datoteke nismo našli, nalagam novo.")
            d = {
                     'stanje': seznam,
                     'zmaga_X': player1,
                     'zmaga_y': player2,
                     'izenaceno': dif,
                     'H': H,
                }
        except:
            messagebox.showwarning("Error", "Problme pri nalaganju datoteke.")
        
                        
okno = tk.Tk()
okno.title("polje")
okno.configure(bg="#f0f0f0")

restart = 0
vrsta = 0
H=0
nasprotnik = ""
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