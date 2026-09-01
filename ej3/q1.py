vueltas = int(input())
n = 1
lista = []
quedan = vueltas - 5
quedan_lista = []



for i in range(vueltas):
    lista.append(n)
    n += 1

for j in range(quedan):
    quedan_lista.append(quedan)
    quedan -= 1


print(lista)
print(quedan_lista)

for item in lista:
    if item <= 5:
        print(f"Vuelta {item}!!!")

for item in quedan_lista:
     print(f"Me quedan {item} vueltas")

print(f"Termine las {vueltas} vueltas")