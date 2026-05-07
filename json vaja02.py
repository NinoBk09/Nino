import json

zaloga = {
    'jabolka': 10,
    'banane': 5,
    'maline': 20,
    'kiwi': 12,
    }

with open('trgovina.josn', 'w') as f:
    json.dump(zaloga,f)

try:
    with open('trgovina.josn', 'r') as f:
        zaloga = json.load(f)
    print("podatki uspešno naloženi")
except FileNotFoundError:
    print("nenajdem datoteke, nalagam novo: ")
    zaloga = {}

zaloga['hruška'] = 20

print(f"{zaloga}")