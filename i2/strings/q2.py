# 20 min

string = input()
lista = []

for char in string:
    lista.append(char)

i = 0

while i < len(lista)-1:
    if lista[i] == lista[i+1]:
        lista.pop(i)
    else:
        i += 1



for char in lista:
    print(char, end="")