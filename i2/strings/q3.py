def suenos_repetidos(loop):
    lista = []

    
    for j in range(len(loop)):
        for i in range(len(loop)):
            lista.append(loop[i:j+1])

    k = 0
    while k < len(lista):
        if len(lista[k]) <=1:
            lista.pop(k)
        else:
            k+=1
    
    
    ocurrencias_sucio = []

    for item in lista:
        apps = lista.count(item)
        ocurrencias_sucio.append([item, apps, len(item)])

    ocurrencias = []

    for item in ocurrencias_sucio:
        if item not in ocurrencias:
            ocurrencias.append(item)

    ocurrencias.sort(key=lambda x: x[1], reverse=True)

    h = 0
    while h < len(ocurrencias):
        if ocurrencias[h][1] < ocurrencias[0][1]:
            ocurrencias.pop(h)
        else:
            h += 1

    ocurrencias.sort(key=lambda x: x[2], reverse=True)


    




    return(ocurrencias[0][0])
    


        


print(suenos_repetidos("xyzxyzx"))