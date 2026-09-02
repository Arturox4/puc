n = 0
total = 0

while True:
    nombre = input()
    if nombre == "CERRADO":
       break
    n += 1
    cantidad = int(input())

    for i in range(cantidad):
        precio = int(input())
        total += precio

    print(f"{nombre} compro {cantidad} items por {total}")
    total = 0

print(n)


    