enemigo = input()
ls_enemigos = []



while enemigo != "FIN":
    ls_enemigos.append(enemigo)
    enemigo = input()

ls_enemigos_prima = ls_enemigos


indice = int(input())



print(f"{ls_enemigos.pop(indice)} fue atacado!")


for item in ls_enemigos:
    print(item)

final_lista = []

for i in range(2):
    final_lista.append(ls_enemigos_prima[i])

rango = len(ls_enemigos_prima) - 1

final_lista.append(ls_enemigos_prima[rango])
rango += 1
final_lista.append(ls_enemigos_prima[rango])

print(final_lista)



