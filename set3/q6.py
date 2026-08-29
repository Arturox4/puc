fuerza_base = int(input())
dist_min = int(input())

distancia = 1
sumas = []
n = 1
sumas.append(int(1))

while True:
    if n % 2 == 0:
        distancia = distancia + fuerza_base**n
        actual = fuerza_base**n
    else:
        distancia = distancia + -(fuerza_base**n)
        actual = -(fuerza_base**n)
    

    sumas.append(actual)

    if sum(sumas) >= dist_min:
        break
    n += 1


acumulado = 0
operaciones = []


for item in sumas:
    acumulado += item
    operaciones.append(str(item))
    print(" + ".join(operaciones), "=", acumulado)

print(f"Necesite {len(sumas)} golpes para alcanzar los {dist_min} metros")