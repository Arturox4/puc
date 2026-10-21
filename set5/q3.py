frase = input()
mayus = 0
minus = 0
numero = 0
raro = 0

for char in frase:
    if char in "ABCDEFGHIJKLMÑOPQRTSUVWXYZ":
        mayus += 1
    elif char in "abcdefghijklmnñopqrstuvwxyz":
        minus += 1
    elif char in "1234567890":
        numero += 1
    else: 
        raro = 1

if raro == 1:
    print("01111001 01100001")

if mayus > 0 and minus == 0 and raro == 0:
    print(frase.lower())
if mayus == 0 and minus > 0 and raro == 0:
    print(frase.upper())
if mayus > 0 and minus > 0 and raro == 0:
    print(frase)








