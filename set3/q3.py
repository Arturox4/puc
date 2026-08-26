vida = int(input())
daño = int(input())
disparos = int(input())

for i in range(disparos):
    print("BANG!")
    vida = vida - daño
    daño += 1
print("clack, clack, boom!")
print(vida)

 
