X = int(input())
lista = []
matriz = []

for i in range(X):
    lista.append(input())

for item in lista:
    matriz.append(item.split(" "))

def quitar_comas(palabra):
    palabra_lista = palabra.split(",")

    return "".join(palabra_lista)
       
indice = int(matriz[0][0])

print(quitar_comas(matriz[0][1]), end="")



for i in range(X-1):
    if indice == -1:
        break

    
    print(quitar_comas(matriz[(indice)][1]), end="")
    indice = int(matriz[indice][0])



