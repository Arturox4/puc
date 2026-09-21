import math as m

angulo = int(input())
angulo_rad = m.radians(angulo)

x = round(m.cos(angulo_rad), 2)
y = round(m.sin(angulo_rad), 2)

print(x)
print(y)

print(int(angulo/360))




