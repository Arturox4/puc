string = input()

personas = string.split(";")
matriz = []
matriz_nueva = []


for item in personas:
    matriz.append(item.split(","))





for i in range(len(matriz)):
    id = matriz[i][0]
    cat_pref = matriz[i][1]
    es_colado = matriz[i][2]
    if (cat_pref != "Nada") and es_colado == "No":
        matriz_nueva.append([id, cat_pref, es_colado])


for i in range(len(matriz)):
    id = matriz[i][0]
    cat_pref = matriz[i][1]
    es_colado = matriz[i][2]
    if (cat_pref == "Nada") and es_colado == "No":
        matriz_nueva.append([id, cat_pref, es_colado])

for i in range(len(matriz)):
    id = matriz[i][0]
    cat_pref = matriz[i][1]
    es_colado = matriz[i][2]
    if (cat_pref != "Nada") and es_colado != "No":
        matriz_nueva.append([id, cat_pref, es_colado])


for i in range(len(matriz)):
    id = matriz[i][0]
    cat_pref = matriz[i][1]
    es_colado = matriz[i][2]
    if (cat_pref == "Nada") and es_colado != "No":
        matriz_nueva.append([id, cat_pref, es_colado])



for i in range(len(matriz_nueva)):
    print(matriz_nueva[i])






