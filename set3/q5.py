lower = int(input())
upper = int(input())

print("Buscando estrellas brillantes...")

divisores = []
estrellas = []
q_lista = []
rango = upper - lower
total = 0
lower_og = lower

for i in range(rango + 1):
    if lower % 2 == 0:

        for j in range(1, lower):
            if lower % j == 0:
                divisores.append(j)
            total = sum(divisores)
            
            
        if total >= 16:
            estrellas.append(lower)
            q_lista.append(total)

        total = 0
        divisores.clear()
                        
    lower += 1

ñ = 0

for k in estrellas:
    p = abs(k - lower_og)
    q = q_lista[ñ]
    r = abs(upper - k)
    print("Encontre una estrella brillante!")
    print(f"Coordenadas: {p} {q} {r}")
    ñ += 1

