def emparejar_pilotes(pilotes):

    alturas = []
    pos_grietas = []

    for i in range(len(pilotes[0])):
        
        altura = 0
        grieta = 0
        for j in range(len(pilotes)):
            
            if pilotes[j][i] == "p" or pilotes[j][i] == "x":
                altura += 1
            if pilotes[j][i] == "x":
                grieta += 1
                pos_grietas.append([j,i])  


        # i es pos original
        alturas.append([altura, grieta, i])



    alturas.sort(key=lambda x: x[0])
    altura_min = 0

    # Encontrar a que nivel nivelar
    for i in range(len(alturas)):
        if alturas[i][0] != 0 and alturas[i][1] < 2:
            altura_min = alturas[i][0]
            break
        
    # Nivela y saca los pilotes con grieta >= 2
    for i in range(len(alturas)):
        if alturas[i][0] != 0 and alturas[i][0] > altura_min and alturas[i][1] < 2:
            alturas[i][0] = altura_min  
        elif alturas[i][1] >= 2:
            alturas[i][0] = 0
            alturas[i][1] = 0


    alturas.sort(key=lambda x: x[2], reverse=False)

    matriz = []
    # Crear matrix Vacia
    for i in range(len(pilotes)):
        matriz.append([])
        for j in range(len(pilotes[0])):
            matriz[i].append("-")

    

    # colocar grietas
    for cords in pos_grietas:
        fila = cords[0]
        columna = cords[1]
        if fila >= len(matriz) - alturas[columna][0]:
            matriz[fila][columna] = "x"

    # revisa cada poscion de Matriz y decide por que remplazar el valor
    for columna in range(len(matriz[0])):

        for fila in range(len(matriz)):

            # Remplaza todas las columnas altura 0 por -
            if alturas[columna][0] == 0:
                matriz[fila][columna] = "-"

            # si la fila actual es menor al alto - la altura colocar p
            if fila >= len(matriz) - alturas[columna][0] and matriz[fila][columna] != "x":
                matriz[fila][columna] = "p"

    return matriz


    
        
            
            