def embocando(habilidad1, habilidad2):
    turno = 1
    while True:
        destreza = 0
        suerte = float(input())

        if turno % 2 != 0:
            destreza = habilidad1 + suerte
            print(f"Destreza yo: {destreza}")
            habilidad1 = habilidad1 *1.5
            if destreza >= 100:
                return "yo"
                break            
        else:
            destreza = habilidad2 + suerte
            print(f"Destreza DCCondorito: {destreza}")
            habilidad2 = habilidad2 *1.5
            if destreza >= 100:
                return "DCCondorito"
                break
        turno += 1 


        