fuerza_base = int(input())
dist_min = int(input())
distancia = 1
sumas = []
n = 1


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

print(sumas)