import json

profil = {
    "ime": "Gamer123",
    "level": 5,
    "tocke": 1500
    }

#shrani
with open('file.json', 'w') as f:
    json.dump(profil,f)
    
#spremeni v string
p = json.dumps(profil)

print(p)

#nalaganje igre
with open('file.json', 'r') as l:
    podatki = json.load(l)

#spremenim podatke
podatki["level"] += 1
podatki["tocke"] += 500
#shranim igro
with open('file.json','w') as f:
    json.dump(podatki,f)
#spremenim v string
p = json.dumps(podatki)
print(p)

seznam=["pospravi sobo","nariši sliko","pobriši prah"]

with open('file.json', 'w') as f:
    json.dump(seznam,f)


try:
    with open('file.json','r') as f:
        todo = json.load(f)
    print("Podatki naloženi!")
except FileNotFoundError:
    print("datoteka ne obstaja, nalagam novo.")
    podatki = []
for i in range(len(todo)):
    print(f"{i+1}. {todo[i]}")