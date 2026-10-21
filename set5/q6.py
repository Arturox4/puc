frase = input()
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






    
