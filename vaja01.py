from tkinter import *
def izpis():
    for i in range(3):
        for u in range(3):
            print(seznam[u+i*3], end="  ")
        for _ in range(2):
            print()
            
def zmaga(seznam):
    x=0
    vrstice=[[0,1,2],[3,4,5],[6,7,8]]
    stolpci=[[0,3,6],[1,4,7],[2,5,8]]
    diagonale=[[0,4,8],[2,4,6]]
    for i in vrstice:
        if seznam[i[0]] == seznam[i[1]] == seznam[i[2]] == "X":
            return " ZMAGA X"
        elif seznam[i[0]] == seznam[i[1]] == seznam[i[2]] == "O":
            return " ZMAGA O"
        
    for i in stolpci:
        if seznam[i[0]] == seznam[i[1]] == seznam[i[2]] == "X":
            return " ZMAGA X"
        elif seznam[i[0]] == seznam[i[1]] == seznam[i[2]] == "O":
            return " ZMAGA O"
        
    for i in diagonale:
        if seznam[i[0]] == seznam[i[1]] == seznam[i[2]] == "X":  
            return " ZMAGA X"
        elif seznam[i[0]] == seznam[i[1]] == seznam[i[2]] == "O":
            return " ZMAGA O"
    return "ne"
znaka=["X","O"]
while True:
    seznam=["1","2","3","4","5","6","7","8","9"]
    for i in range(len(seznam)):
        if i == 2 or i == 5:
            print(seznam[i])
        else:
            print(seznam[i], end=" ")
    print()       
    for i in range(len(seznam)):
        if i%2==0:
            a=int(input("Vnesi X: "))
            if seznam[a-1] in znaka:
                print("polje že zasedeno")
                continue
            seznam[a-1] = "X"
            izpis()
            rezultat = zmaga(seznam)
            if rezultat != "ne":
                print(f"{rezultat}! \n <----------------> \n ZAČETEK NOVE IGRE!")
                break
                
        else:
            b=int(input("Vnesi O: "))
            if seznam[b-1] in znaka:
                print("polje že zasedeno")
                continue
            seznam[b-1] = "O"
            izpis()
            rezultat = zmaga(seznam)
            if rezultat != "ne":
                print(f"{rezultat}! \n <-------------> \n ZAČETEK NOVE IGRE!")
                break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    




        