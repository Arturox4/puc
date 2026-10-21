string = input()

barra = string.split("/")

matriz = []

for item in barra:
    lista = item.split(",")
    matriz.append(lista)



for i in range(4):

    fila = int(input())
    columna = int(input())

    matriz[fila][columna] = "X"


for i in range(len(matriz)):
    print(matriz[i])

    

