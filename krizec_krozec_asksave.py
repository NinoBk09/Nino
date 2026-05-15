import tkinter as tk
import json
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import random

def izbira_O():
    global board
    opponent_O = ""
    two_in_row_0 = [[3,6],[4,8],[1,2]]
    two_in_row_1 = [[0,2],[4,7]]
    two_in_row_2 = [[4,6],[5,8],[0,1]]
    two_in_row_3 = [[0,6],[4,5]]
    two_in_row_4 = [[1,7],[3,5],[0,8],[2,6]]
    two_in_row_5 = [[3,4],[2,8]]
    two_in_row_6 = [[0,3],[2,4],[7,8]]
    two_in_row_7 = [[1,4],[6,8]]
    two_in_row_8 = [[6,7],[0,4],[2,5]]

#preveri zmago             
    for i in two_in_row_0:
        if board[i[0]] == board[i[1]] == "O":
            opponent_O = 0
            if board[opponent_O] == "":    
                return opponent_O
#preveri zmago
    for i in two_in_row_1:
        if board[i[0]] == board[i[1]] == "O":
            opponent_O = 1
            if board[opponent_O] == "":    
                return opponent_O
#preveri zmago
    for i in two_in_row_2:
        if board[i[0]] == board[i[1]] == "O":
            opponent_O = 2
            if board[opponent_O] == "":    
                return opponent_O
#preveri zmago
    for i in two_in_row_3:
        if board[i[0]] == board[i[1]] == "O":
            opponent_O = 3
            if board[opponent_O] == "":    
                return opponent_O
#preveri zmago
    for i in two_in_row_4:
        if board[i[0]] == board[i[1]] == "O":
            opponent_O = 4
            if board[opponent_O] == "":    
                return opponent_O
#preveri zmago
    for i in two_in_row_5:
        if board[i[0]] == board[i[1]] == "O":
            opponent_O = 5
            if board[opponent_O] == "":    
                return opponent_O
#preveri zmago
    for i in two_in_row_6:
        if board[i[0]] == board[i[1]] == "O":
            opponent_O = 6
            if board[opponent_O] == "":    
                return opponent_O
#preveri zmago
    for i in two_in_row_7:
        if board[i[0]] == board[i[1]] == "O":
            opponent_O = 7
            if board[opponent_O] == "":    
                return opponent_O
#preveri zmago
    for i in two_in_row_8:
        if board[i[0]] == board[i[1]] == "O":
            opponent_O = 8
            if board[opponent_O] == "":    
                return opponent_O
#preveri blokado
    for i in two_in_row_0:
        if board[i[0]] == board[i[1]] == "X":
            opponent_O = 0
            if board[opponent_O] == "":    
                return opponent_O
#preveri blokado
    for i in two_in_row_1:
        if board[i[0]] == board[i[1]] == "X":
            opponent_O = 1
            if board[opponent_O] == "":    
                return opponent_O
#preveri blokado
    for i in two_in_row_2:
        if board[i[0]] == board[i[1]] == "X":
            opponent_O = 2
            if board[opponent_O] == "":    
                return opponent_O
#preveri blokado            
    for i in two_in_row_3:
        if board[i[0]] == board[i[1]] == "X":
            opponent_O = 3
            if board[opponent_O] == "":    
                return opponent_O
#preveri blokado
    for i in two_in_row_4:
        if board[i[0]] == board[i[1]] == "X":
            opponent_O = 4
            if board[opponent_O] == "":    
                return opponent_O
#preveri blokado
    for i in two_in_row_5:
        if board[i[0]] == board[i[1]] == "X":
            opponent_O = 5
            if board[opponent_O] == "":    
                return opponent_O
#preveri blokado
    for i in two_in_row_6:
        if board[i[0]] == board[i[1]] == "X":
            opponent_O = 6
            if board[opponent_O] == "":    
                return opponent_O
#preveri blokado
    for i in two_in_row_7:
        if board[i[0]] == board[i[1]] == "X":
            opponent_O = 7
            if board[opponent_O] == "":    
                return opponent_O
#preveri blokado
    for i in two_in_row_8:
        if board[i[0]] == board[i[1]] == "X":
            opponent_O = 8
            if board[opponent_O] == "":    
                return opponent_O
    while True:
        opponent_O = random.randint(0,8)
        if playing_field[opponent_O]['text'] == '':
            return opponent_O
    
def klik(i):    
    global playing_field, player, board, d, X_wins, O_wins, draw, heuristics, turn_X_O , restart, reset_O_start, win_row
    heuristics = 0
    stop_if_draw = ""
    heuristics_regulation_3_3 = 0
    if turn_X_O  ==  True:
        if playing_field[i]["text"] == "":
            heuristics_regulation_3_3 += 1
            board[i] = player
            playing_field[i]["text"] = board[i]
            stop_if_draw = draw()
            if stop_if_draw == True:
                return None
        turn_X_O  = False
        heuristics_function()

    dont_place_O = win()
    if dont_place_O == True:
        return
#Nasprotnik   
    if heuristics_regulation_3_3 == 1 or reset_O_start == 0:
        reset_O_start = 1
        if turn_X_O  == False:
            opponent_O = izbira_O()
            board[opponent_O] = "O"
            playing_field[opponent_O]["text"] = board[opponent_O]
            stop_if_draw = draw()
            if stop_if_draw == True:
                return None
        heuristics_function()
        win()
    turn_X_O  = True
    
    d = {
        'stanje': board,
        'win_X': X_wins,
        'win_O': O_wins,
        'draw': draws,
        'heuristics': heuristics,
        'na_vrsti': turn_X_O ,
        'zacne': restart,
        }
        
def win():
    global playing_field, X_wins, O_wins, turn_X_O, heuristics_regulation_3_3, win_row
    for k in win_row:
        if playing_field[k[0]]["text"] == "X" and playing_field[k[1]]["text"] == "X" and playing_field[k[2]]["text"] == "X":
            X_wins += 1
            winer = "X"
            d['win_X'] = X_wins
            label_x.config(text=f"X zmage: {X_wins}")
            label.config(text=f"Zmaga {winer}", fg="lightgreen") 
            for g in playing_field:
                g.config(state="disable")
            heuristics_regulation_3_3 = 0
            return True
    for k in win_row:
        if playing_field[k[0]]["text"] == "O" and playing_field[k[1]]["text"] == "O" and playing_field[k[2]]["text"] == "O":
            O_wins += 1
            winer = "O"
            d['win_O'] = O_wins
            label_o.config(text=f"O zmage: {O_wins}")
            label.config(text=f"Zmaga {winer}", fg="lightgreen") 
            for g in playing_field:
                g.config(state="disable")
            heuristics_regulation_3_3 = 0
        
def heuristics_function():
    global playing_field, win_row, heuristics, playing_field, board
    
    heuristics = 0
    for i in win_row:
        if (playing_field[i[0]]['text'] == "X" and playing_field[i[1]]['text'] == "" and playing_field[i[2]]['text'] == "") or (playing_field[i[1]]['text'] == "X" and playing_field[i[0]]['text'] == "" and playing_field[i[2]]['text'] == "") or (playing_field[i[2]]['text'] == "X" and playing_field[i[0]]['text'] == "" and playing_field[i[1]]['text'] == ""):
            heuristics+=1
        if (playing_field[i[0]]['text'] == "X" and playing_field[i[1]]['text'] == "X" and playing_field[i[2]]['text'] == "") or (playing_field[i[1]]['text'] == "X" and playing_field[i[2]]['text'] == "X" and playing_field[i[0]]['text'] == "") or (playing_field[i[2]]['text'] == "X" and playing_field[i[1]]['text'] == "X" and playing_field[i[1]]['text'] == ""):
            heuristics+=10
        if playing_field[i[0]]['text'] == "X" and playing_field[i[1]]['text'] == "X" and playing_field[i[2]]['text'] == "X":
            heuristics+=99999
        if (playing_field[i[0]]['text'] == "O" and playing_field[i[1]]['text'] == "" and playing_field[i[2]]['text'] == "") or (playing_field[i[1]]['text'] == "O" and playing_field[i[0]]['text'] == "" and playing_field[i[2]]['text'] == "") or (playing_field[i[2]]['text'] == "O" and playing_field[i[0]]['text'] == "" and playing_field[i[1]]['text'] == ""):
            heuristics-=1
        if (playing_field[i[0]]['text'] == "O" and playing_field[i[1]]['text'] == "O" and playing_field[i[2]]['text'] == "") or (playing_field[i[1]]['text'] == "O" and playing_field[i[2]]['text'] == "O" and playing_field[i[0]]['text'] == "") or (playing_field[i[2]]['text'] == "O" and playing_field[i[1]]['text'] == "O" and playing_field[i[1]]['text'] == ""):
            heuristics-=10
        if playing_field[i[0]]['text'] == "O" and playing_field[i[1]]['text'] == "O" and playing_field[i[2]]['text'] == "O":
            heuristics-=99999
    print(f"heuristics je: {heuristics}, board: { board }")
    return heuristics

def reset():
    global player, board, heuristics, restart, turn_X_O , reset_O_start
    if restart == 1:
        zacne = "O"
        turn_X_O  = False
        reset_O_start = 0
        restart = 0
    else:
        zacne = "X"
        turn_X_O  = True
        restart = 1
    label_zacetek.config(text=f"Začne: {zacne}") 
    label.config(text="")
    for gumb in playing_field:
        gumb.config(text="", state="normal")
    for i in range(len(board)-1,-1,-1):
        if board[i] != "":
            board[i] = ""
    print(board)
    label.config(bg="#f0f0f0")
    heuristics = 0

        
def draw():
    global board, draws, d, X_wins, turn_X_O 
    if board.count("") == 0:
        draws += 1
        d['draw'] = draws
        label_draw.config(text=f"izenačeno: {draws}")
        label.config(text="Izenačeno", bg="yellow")
        for g in playing_field:
            g.config(state="disable")
        return True
            
def shrani():
    global d
    
    d = {
        'stanje': board,
        'win_X': X_wins,
        'win_O': O_wins,
        'draw': draws,
        'heuristics': heuristics,
        'na_vrsti': turn_X_O ,
        'zacne': restart,
        }
    
    files = [('JSON dokument', '*.json'), ('Vse datoteke', '*.*')]
    file = asksaveasfile(filetypes=files, defaultextension=".json")
    json.dump(d,file)
    file.close()   
    label.config(text="Shranjeno", bg="lightgreen")

def nalozi():
    global d, board, draws, O_wins, X_wins, heuristics
    file = askopenfile(filetypes=[('JSON dokument', '*.json'), ('Vse datoteke', '*.*')])
    if file:
        try: 
            d = json.load(file)
            board = d['stanje']
            for i in range(9):
                    playing_field[i].config(text=board[i],state="normal")
            z = win()
            if z == "X" or z == "O":
                board = ["","","","","","","","",""]
                for i in range(9):
                    playing_field[i].config(text=board[i],state="normal")
            label_draw.config(text=f"izenačeno: {d['draw']}")
            label_o.config(text=f"O zmage: {d['win_O']}")
            label_x.config(text=f"X zmage: {d['win_X']}")
            X_wins = d['win_X']
            O_wins = d['win_O']
            draws = d['draw']
            heuristics = d['heuristics'] 
            label.config(text="datoteka uspešno naložena", bg="lightgreen", fg="white")
            file.close()
        except FileNotFoundError:
            messagebox.showwarning("Error", "Datoteke nismo našli, nalagam novo.")
            d = {
                'stanje': board,
                'win_X': X_wins,
                'win_O': O_wins,
                'draw': draws,
                'heuristics': heuristics,
                'na_vrsti': turn_X_O ,
                'zacne': restart,
                }
        except:
            messagebox.showwarning("Error", "Problme pri nalaganju datoteke.")
        
                        
okno = tk.Tk()
okno.title("polje")
okno.configure(bg="#f0f0f0")

win_row = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
reset_O_start = 1
restart = 1
turn_X_O  = True
heuristics=0
opponent_O = ""
X_wins = 0
O_wins = 0
draws = 0
playing_field=[]
player = "X"
d=0

label_zacetek = tk.Label(okno, text=f"Začne: {player}", height=3, width=9, font=("Arial", 15, "bold"), bg="#E6E6E6",relief="flat")
label_zacetek.pack()

frame_playing_field = tk.Frame(okno)
frame_playing_field.pack(pady=10)

for i in range(9):
    gumb = tk.Button(frame_playing_field, height=3, width=6, command=lambda i=i: klik(i), bg="#cccccc", font=("Arial", 15, "bold"))
    gumb.grid(row=i//3, column=i%3,)
    playing_field.append(gumb)

frame_spodaj = tk.Frame(okno)
frame_spodaj.pack(pady=20)

gumb1 = tk.Button(frame_spodaj, height=3, width=9,bg="#687982", command=reset, text="Nova igra", fg="white",  relief="flat", bd=0, highlightthickness=0,font=("helvetica", 10, "bold"))
gumb1.grid(column=1, row=0, padx=5)

button_save = tk.Button(frame_spodaj, height=3, width=9,bg="#688271", fg="white", command=shrani, text="Shrani", relief="flat", bd=0, font=("helvetica", 10, "bold"), highlightthickness=0)
button_save.grid(column=2, row=0, padx=5)

button_load = tk.Button(frame_spodaj, text="Naloži", height=3, width=9, bg="#716882", fg="white", command=nalozi, relief="flat", bd=0, font=("helvetica", 10, "bold"), highlightthickness=0)
button_load.grid(column=3, row=0, padx=5)

frame_label = tk.Frame(okno)
frame_label.pack(pady=10,)

label = tk.Label(frame_label, text="", pady="10",font=("helvetica", 14, "bold"))
label.grid(column=2, row=1)

frame_rezultat = tk.Frame(okno)
frame_rezultat.pack()

label_x = tk.Label(frame_rezultat, text=f"X zmage: {X_wins}", height=3, width=9, font="Segoe_UI",)
label_x.grid(row=0,column=0, sticky="w")

label_o = tk.Label(frame_rezultat, text=f"O zmage: {O_wins}", height=3, width=9, font="Segoe_UI")
label_o.grid(row=1,column=0, sticky="w")

label_draw = tk.Label(frame_rezultat, text=f"izenačeno: {draws}", height=3, width=9, font="Segoe_UI")
label_draw.grid(row=2,column=0, sticky="w")

board = ["","","","","","","","",""]
okno.mainloop()