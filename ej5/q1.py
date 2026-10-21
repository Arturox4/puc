palabra = input()


while "!" in palabra:
    for char in palabra:
        if char in "!":
            palabra = palabra.replace(char, "")

    print(palabra)
    palabra = input()
print(palabra)