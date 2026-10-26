def juego_lagartija(juego, jugadores):

    pasos_para_ganar = juego[0]

    jugadores_og = []
    jugadores_muertos = []
    
    for item in jugadores:
        jugadores_og.append(item[0])

    print(jugadores_og)
    jugadores_vivos = []

    for turno in range(len(juego[1])):

        # borrar players
        for player in jugadores:
            if juego[1][turno] == "luz roja" and player[1][turno] > 0 and player[turno] <= pasos_para_ganar:
                jugadores_muertos.append(player)

        
    # sacar muertos de jugadores og
    for a in range(len(jugadores)):
        if jugadores[a] not in jugadores_muertos:
            jugadores_vivos.append(jugadores[a])

    


    
    








        
            


                

    print(jugadores_muertos)
    print(jugadores_vivos)

    
                
                

                

