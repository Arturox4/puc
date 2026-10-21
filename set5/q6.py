frase = input()
<<<<<<< HEAD
frase = frase.split()

abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÑñ"


def desencriptar(palabra):
    palabra = list(palabra)

    for letra in abecedario:
        
        if palabra.count(letra) == 2:
            return letra

    return palabra[len(palabra)-1]

for item in frase:
    print(desencriptar(item), end="")






    
=======

palabras = frase.split()
dc = []

for item in palabras:
    for char in item:
        if item.count(char) == 2:
            dc.append(char)
            continue
        if item.count(char) == 1:
            dc.append(item[len(item)-1])
            continue
print(dc)
>>>>>>> aa7665e81405883cd02f1afb4170cddaeec9fd81
