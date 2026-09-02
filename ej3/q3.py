revisar = int(input())
n = 1
j = 1

for i in range(revisar):
    nombre = input()

    if nombre == "NO ESTA":
        esta = input()
        while esta == "NO":
            print(f"NO ESTA EN {j}")
            j += 1
            esta = input()
            if j > 5:
                print("SE ESCAPO")
                n -= 1
                break
    if nombre != "NO ESTA":
        print(f"{n} - {nombre}")

            
    n += 1    



print(f"Hay {n} de {revisar} reos")
