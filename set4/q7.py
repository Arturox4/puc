import q6 

contraseña_og = input()
digitos_a_encriptar = int(input())
contraseña_og_lista = []


for i in range(len(contraseña_og)):
    contraseña_og_lista.append(contraseña_og[i])

contraseña_og = int(contraseña_og)
print(contraseña_og_lista)

if q6.cantidad_de_digitos(contraseña_og) % 2 == 0:
    reversa = True
else:
    reversa = False

ultimo_digito_lista = []

for j in range(digitos_a_encriptar):
    numero = q6.en_posicion(contraseña_og, j, reversa)
    numero = numero +2
    numero = numero**numero
    numero_string = str(numero)

    for k in range(q6.cantidad_de_digitos(numero)):
        ultimo_digito_lista.append(numero_string[k])
        ultimo_digito = int(ultimo_digito_lista[k])

    contraseña_og = int(contraseña_og)
    contraseña_og = q6.reemplazar(contraseña_og, j, ultimo_digito, reversa)
    numero = 0
    ultimo_digito_lista.clear()



print(contraseña_og)



    




