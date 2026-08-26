numero = input()

a = int(numero[0])
b = int(numero[1])
c = int(numero[2])
d = int(numero[3])
e = int(numero[4])

wnumero = int(numero)

regla1 = int(d*10 + e)

if regla1  != 0 and wnumero % regla1 == 0:
    print("True")
else:
    print("False")

print(a < c)
print(b > e)
print(d <= e)

if a < c and b > e and d <= e and regla1  != 0 and wnumero % regla1 == 0:
    print("LENNY!")
else:
    print("NOT LENNY!")
