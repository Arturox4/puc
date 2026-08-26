numero = input() 

a = int(numero[0])
b = int(numero[1])
c = int(numero[2])
d = int(numero[3])
e = int(numero[4])
f = int(numero[5])
g = int(numero[6])
h = int(numero[7])

inicio = a*100 + b*10 + c
final  = f*100 + g*10 + h

horas = int(input())
minutos = int(input())

hora = horas*100 + minutos
print(hora)


if hora <= 820:
    print("CONTESTAR EMERGENCIA")
elif hora < 1300:
    if final == 909:
        print("CONTESTAR 909")
    else:
        print("NO CONTESTAR 8:20-13:00")    
elif hora < 1950:
    if inicio == 877:
        print("NO CONTESTAR 877")
    else:
        print("CONTESTAR 13:00-19:50")
else:
    print("NO CONTESTAR 19:50-00:00")


    

