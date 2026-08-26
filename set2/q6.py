final =  int(input())
inicial = int(input())

resta = final - inicial
restaB = 100 - abs(resta)

if resta <= 50 and resta > 0:
    print(f"{resta} veces arriba")
elif resta > 50 and resta > 0:
    print(f"{restaB} veces abajo")

if resta >= -50 and resta < 0:
    print(f"{abs(resta)} veces abajo")
elif resta < -50 and resta < 0:
    print(f"{restaB} veces arriba")