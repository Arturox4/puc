def cantidad_de_digitos(numero):
    string = str(numero)
    n = len(string)
    return n

def en_posicion(numero, indice, reversa):
    string = str(numero)
    length = len(string)   

    if reversa == True:
        n = length - (indice + 1)
        obj = int(string[n])
    if reversa == False:
        obj = int(string[indice])

    return obj




def reemplazar(numero, indice, nuevo, reversa):

    digitos = list(str(numero))

    if reversa == True:
        posicion = len(digitos) - 1 - indice
    else:
        posicion = indice

    digitos[posicion] = str(nuevo)

    return int("".join(digitos)) 




    

    





    

