balas = int(input())

msg = input()

while msg == "There you go!":
    for i in range(balas):
        print("BANG!")
    print("Recargando", end="")
    for i in range(balas - 1):
        print(".", end="")
    print(".")
    msg = input()
    
print("Te perdono por tus pecados, fuera de mi pueblo")