for i in range(int(input())):
    dialogo = input()
    dialogo = dialogo.split(":")

    persona = dialogo[0]

    dialogo = dialogo[1]
    dialogo = dialogo.split()

    for i in range(len(dialogo)-2):

        if dialogo[i:i+3] == ["yo", "no", "fui"]:
            culpable = persona
            print(f"Impostor: {culpable}")

    
for i in range(int(input())):

    if culpable in dialogo:
        dialogo = dialogo.split(":")
        dialogo = dialogo[1]
        dialogo = dialogo.split()
        
        for item in dialogo:
            
            if item == "pasillo":
                print(f"Ultima posicion: Pasillo {dialogo[dialogo.index(item)+1]}")    


