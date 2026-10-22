def mostrar_estado_gato(tablero):
    
    lista = ["X", "O"]
    for fila in tablero:
        print(" ".join(fila))
        

    for i in range(3):

        for item in lista:    
            if tablero[i] == [item, item, item]:
                return print(f"Ganador: {item}")
            
            elif tablero[0][i] == item and tablero[1][i] == item and tablero[2][i] == item:
                return print(f"Ganador: {item}")

            elif tablero[0][0] == item and tablero[1][1] == item and tablero[2][2] == item:
                return print(f"Ganador: {item}")
            
            elif tablero[0][2] == item and tablero[1][1] == item and tablero[2][0] == item:
                return print(f"Ganador: {item}")


    for fila in tablero:
        if "-" in fila:
                return print("No ha terminado")
    else:
        print("Empate")
    










        