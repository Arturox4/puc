vueltas = int(input())
n = 1
lista = []
quedan_ = vueltas - 5
quedan = []



for i in range(vueltas):
    lista.append(n)
    n += 1

for j in range(len(quedan)):
    quedan.append(quedan)
    quedan -= 1


print(lista)

for item in lista:
    if item <= 5:
        print(f"Vuelta {item}!!!")

    if item > 5: 
        print(f"Me quedan {quedan} vueltas")
        quedan_ -= 1