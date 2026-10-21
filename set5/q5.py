frase = input()
frase = frase.replace(",",".")

lista_frase = []


for char in frase:
    lista_frase.append(char)
        

inicio = lista_frase.index(".")
final = lista_frase.index(".", inicio+1)

for i in range(inicio+1,final):
    print(lista_frase[i], end="")

print()
print(f"Posiciones {inicio} - {final}")