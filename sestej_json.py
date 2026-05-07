import tkinter as tk
import json
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile

def povecaj():
    global x, d
    
    x+=1
    d = {
        'stevilo': x
        }
    label.config(text=f"x = {d['stevilo']}")
    
    with open('file.json', 'w') as f:
        json.dump(d,f)


okno = tk.Tk()
okno.title("counter")

try:
    with open('file.json', 'r') as f:
        d = json.load(f)
        x = d['stevilo']
except (FileNotFoundError, json.JSONDecodeError):
    x = 0
    d = {
        'stevilo': x
        }

label = tk.Label(okno, text=f"x = {d['stevilo']}", height=6, width=10, pady=10)
label.pack()

gumb = tk.Button(okno, text="+1", command=povecaj, pady=5)
gumb.pack()
okno.mainloop()
