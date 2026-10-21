palabra = input()
letra = input()
numero = int(input())

nueva = []
ordenada = []



for char in palabra:
    if char in "AEIOUaeiou":
        nueva.append(letra)
    else:
        nueva.append(char)



for i in range(len(palabra) - numero):
    ordenada.append(nueva[numero+i])

for j in range(numero):
    ordenada.append(nueva[j])


for item in ordenada:
    print(item, end="")