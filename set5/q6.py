frase = input()

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